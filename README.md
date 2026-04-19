# 🪄 AI Background Remover

A full-stack web app for AI-powered image background removal.

## 🚀 Features
- JPG/PNG upload & preview
- AI background removal (rembg U²-Net)
- Transparent PNG download
- Daily limit (2/user)
- User dashboard
- API key auth

## 📂 Structure
```
d:/bg/
├── run.py              # Full-stack entry (python run.py)
├── app/                # Flask app + modules
├── app.html            # Main UI (localhost:5000/)
├── dashboard.html      # Admin dashboard (localhost:5000/dashboard.html)
├── requirements.txt    # Deps
├── Dockerfile          # Docker build
└── docker-compose.yml  # Full stack (optional)
```

## ⚙️ Quick Start (Local)
1. `pip install -r requirements.txt`
2. `python run.py`
3. Open **http://localhost:5000/** (auto-serves app.html)

**API Key:** `bg-be24e8bd47c13f0f5568a2cc6810fd3d`

## 🐳 Docker
```
docker compose up --build
```
- Frontend: http://localhost:80/app.html
- Backend API: http://localhost:5000/api/

## 🔄 Usage
1. Enter API key → Get User ID
2. Upload image → Remove BG → Download PNG
3. Dashboard: localhost:5000/dashboard.html (user stats)

## ⚠️ Notes
- ~170MB model downloads on first run
- In-memory users (resets on restart)
- CPU-only (rembg[cpu])

## 🧠 Purpose
Full-stack AI web app demonstrating ML deployment, auth/limits, Docker.
