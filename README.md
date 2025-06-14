# LifeTriage

**Life Triage** is a voice-first task management app that lets you speak tasks out loud, automatically categorizes them by life domain (e.g. health, work, relationships), and prioritizes them using basic NLP. It's built with **React (Vite)** for the frontend, **Flask (modular)** for the backend, and uses **spaCy** for NLP and **Supabase PostgreSQL** for data storage.

## 🔍 Features

- 🎙 Voice-to-text task capture (Web Speech API)
- 📂 Task categorization by life domain (e.g., health, work)
- 📈 Prioritization based on importance scoring
- 💾 Supabase PostgreSQL for persistent storage
- 🌐 Deployed via Railway (fallback: Render)
- 🔒 Modular and extensible backend architecture

## 🧱 Tech Stack

| Layer       | Technology         |
|------------|--------------------|
| Frontend    | React (Vite), Axios |
| Backend     | Flask, Flask-CORS, Gunicorn |
| NLP         | spaCy (en_core_web_sm) |
| Database    | Supabase PostgreSQL |
| Deployment  | Railway / Render |
| CI/CD       | GitHub Actions (optional) |

## 📁 Project Structure
LifeTriage/
├── api/
│ ├── init.py
│ ├── routes/
│ │ ├── tasks.py
│ │ └── prioritize.py
│ ├── services/
│ │ ├── db.py
│ │ └── nlp.py
│ └── config.py
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── App.jsx
│ │ └── api.js
├── .env
├── requirements.txt
├── Procfile
├── .gitignore



