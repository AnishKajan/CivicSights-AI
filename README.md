# CivicSight AI 🏙️

**CivicSight AI** is a real-time, AI-powered civic issue reporting platform. It enables citizens to report potholes, graffiti, trash, and more via image, audio, or text – while local governments receive auto-classified, geotagged, and prioritized reports.

---

## 🔧 Features

- 🖼️ Image classification with ViT
- 🧠 Zero-shot text classification with BART
- 🗣️ Speech-to-text using Whisper
- 📍 Geolocation tagging and storage
- 🌐 FastAPI backend with React frontend (PWA-ready)
- 📦 Docker + Compose deployment

---

## 📂 Folder Structure

```bash
├── backend/
├── frontend/
├── data/
├── inference/
├── notebooks/
├── docs/

# Clone + Launch
git clone https://github.com/yourusername/civicsight-ai.git
cd civicsight-ai
docker compose up --build

#Then open:
#Backend: http://localhost:8000/docs
#Frontend: http://localhost:3000

curl -X POST http://localhost:8000/api/v1/issues/submit \
  -F "user_id=test_user" \
  -F "latitude=40.7128" \
  -F "longitude=-74.0060" \
  -F "image=@data/sample_inputs/pothole.jpg"
