// frontend/src/pages/ReportForm.jsx
import React, { useState } from 'react'
import axios from 'axios'

const ReportForm = () => {
  const [formData, setFormData] = useState({
    user_id: 'test_user',
    latitude: '',
    longitude: '',
    description: '',
    image: null,
    audio: null,
  })

  const [result, setResult] = useState(null)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData({ ...formData, [name]: value })
  }

  const handleFileChange = (e) => {
    const { name, files } = e.target
    setFormData({ ...formData, [name]: files[0] })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const data = new FormData()
    Object.keys(formData).forEach((key) => {
      if (formData[key]) data.append(key, formData[key])
    })

    try {
      const res = await axios.post('http://localhost:8000/api/v1/issues/submit', data)
      setResult(res.data)
    } catch (err) {
      console.error(err)
      alert('Submission failed')
    }
  }

  return (
    <div>
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        <input type="text" name="latitude" placeholder="Latitude" onChange={handleChange} required />
        <input type="text" name="longitude" placeholder="Longitude" onChange={handleChange} required />
        <textarea name="description" placeholder="Description" onChange={handleChange} />

        <input type="file" name="image" accept="image/*" onChange={handleFileChange} />
        <input type="file" name="audio" accept="audio/*" onChange={handleFileChange} />

        <button type="submit">Submit Issue</button>
      </form>

      {result && (
        <div>
          <h3>Classification Result:</h3>
          <p>Issue: {result.classification}</p>
          <p>Confidence: {result.confidence}</p>
          <p>Status: {result.status}</p>
        </div>
      )}
    </div>
  )
}

export default ReportForm
