# CivicSight AI — React + Vite (Dockerized)

This project uses **React** with **Vite** for frontend development, containerized with Docker for consistent builds and deployment. It also includes a backend powered by FastAPI (see backend folder).

🧩 Project Overview
CivicSight AI is a full-stack web application designed to visualize and analyze AI-driven insights for civic data. The frontend is built with React and bundled using Vite for fast development and hot module reloading. The backend is powered by FastAPI, a modern Python web framework ideal for building high-performance APIs.

🛠 Tech Stack
Languages:

JavaScript (React)

Python (FastAPI)

Frameworks & Libraries:

React — UI component framework

Vite — Frontend build tool and dev server

FastAPI — Lightweight backend web API framework

Axios — HTTP client for frontend-backend communication

Software & Tools:

Docker — Containerizes both frontend and backend for easy deployment

Docker Compose — Manages multi-service architecture

ESLint — Code linting and formatting

npm — JavaScript package manager

---

## ❗ Known Issue: `vite: not found` or `vite needs to be installed` in Docker

If you're seeing errors like this when running `docker compose up`:

```bash
sh: 1: vite: not found
Need to install the following packages:
vite@x.x.x

# How to Run
# Clone
git clone https://github.com/YOUR_USERNAME/civicsight-ai.git
cd civicsight-ai
# Clean Stale Installs
rm -rf node_modules package-lock.json
cd frontend-vite
rm -rf node_modules package-lock.json
cd ..
#Rebuild Docker Containers cleanly
docker compose down -v --remove-orphans
docker compose build --no-cache
docker compose up
#After running docker compose up, visit:
Frontend: http://localhost:5173

Backend: http://localhost:8000

🔧 Dev Stack
React + Vite (frontend)

FastAPI (backend)

Docker + Docker Compose

ℹ️ Original Vite Template Info
This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

#Currently, two official plugins are available:
@vitejs/plugin-react uses Babel for Fast Refresh

@vitejs/plugin-react-swc uses SWC for Fast Refresh

#📦 Future Improvement Ideas
Add TypeScript support

Add Nginx or Caddy for production proxying

Auto-restart frontend/backend with volume mounts