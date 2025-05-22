# CivicSight AI 🏙️🤖

**Note:** This project is incomplete/Needs fixing.

**CivicSight AI** is a real-time, AI-powered civic issue reporting platform. It enables citizens to report potholes, graffiti, trash, and more via image, audio, or text – while local governments receive auto-classified, geotagged, and prioritized reports.

---

## 🔧 Features

- 🖼️ Image classification with ViT
- 🧠 Zero-shot text classification with BART
- 🎙️ Speech-to-text using Whisper
- 📍 Geolocation tagging and storage
- 🌐 FastAPI backend with React frontend (PWA-ready)
- 🐳 Docker + Compose deployment

---

## 🛠️ Tech Stack

- **Languages**: Python, JavaScript (ES6+)
- **Frontend**: React + Vite
- **Backend**: FastAPI
- **AI Models**: ViT (image), BART (text), Whisper (audio)
- **Containerization**: Docker, Docker Compose

---

## ⚠️ Known Issue

> When running `docker compose up`, the frontend may crash with the following error:
>
> ```
> Error: Cannot find module '@rollup/rollup-linux-arm64-gnu'
> ```
> This is due to a [known npm bug](https://github.com/npm/cli/issues/4828) affecting optional dependencies, especially on ARM-based systems like Apple Silicon.

### ✅ Workaround

To resolve this error:

```bash
# Step 1: Go to frontend directory
cd frontend-vite

# Step 2: Clean problematic modules
rm -rf node_modules package-lock.json

# Step 3: Reinstall with safe flags
npm install --legacy-peer-deps --no-optional

# Step 4: Return to root and rebuild
cd ..
docker compose up --build




**🚀 How to Run**
Copy
Edit
# Clone this repo
git clone https://github.com/AnishKajan/CivicSights-AI.git
cd CivicSights-AI

# Build and run containers
docker compose up --build
Then open:

🧠 Backend: http://localhost:8000/docs

🎯 Frontend: http://localhost:5173


**🧪 Test the API**
Submit a sample report to the backend using:

Copy
Edit
curl -X POST http://localhost:8000/api/v1/issues/submit \
-F "user_id=test_user" \
-F "latitude=40.7128" \
-F "longitude=-74.0060" \
-F "image=@data/sample_inputs/pothole.jpg"

**📁 Folder Structure**
kotlin
Copy
Edit
├── backend/
├── frontend-vite/
├── data/
├── inference/
├── notebooks/
├── docs/

**📄 License**
MIT — feel free to fork, improve, and share!
