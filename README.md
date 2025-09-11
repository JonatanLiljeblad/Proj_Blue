Smart Insights Dashboard - (Proj_Blue)

📊 Smart Insights Dashboard is a full-stack web app that combines interactive data visualization with machine learning insights.
Built to explore real sports datasets (NBA / Golf), it predicts player performance and recommends personalized insights — all in a modern, responsive dashboard.

This project showcases full-stack engineering + ML integration + cloud deployment — designed for learning and for portfolio use in data-driven software internships.

⸻

🚀 Features
	•	User Authentication
	•	Sign up / log in (JWT-based)
	•	Save favorite players, teams, or drills
	•	Personalized dashboard
	•	Interactive Dashboard
	•	Explore sports data with filters (season, player, team)
	•	Charts with tooltips & trends over time (Plotly.js/Recharts)
	•	Overview cards for key stats
	•	Machine Learning Insights
	•	Predictive Model: Forecast player performance (e.g., next-game points)
	•	Recommendation System: Suggest players or drills based on user history
	•	API-powered, real-time updates
	•	Full-Stack Tech
	•	Frontend: Next.js + TailwindCSS + Plotly.js/Recharts
	•	Backend: FastAPI (Python) with REST APIs
	•	Database: PostgreSQL (users, stats, predictions, favorites)
	•	ML: Scikit-learn, Pandas, NumPy
	•	Deployment: Vercel (frontend), Heroku/AWS (backend + DB), Docker

⸻

📂 Project Structure

smart-insights-dashboard/
│
├── client/           # Frontend (Next.js, Tailwind, charts)
├── server/           # Backend (FastAPI, ML endpoints, auth)
├── ml/               # ML training scripts, notebooks, saved models
├── data/             # Raw + processed datasets
├── docs/             # Architecture diagrams, notes, screenshots
└── README.md


⸻

🛠️ Tech Stack

Layer	Tech
Frontend	Next.js, TailwindCSS, Plotly.js, Recharts
Backend	FastAPI (Python), REST API
Database	PostgreSQL
ML / Data	Pandas, NumPy, Scikit-learn, Surprise (CF)
Deployment	Vercel (frontend), Heroku/AWS (backend), Docker


⸻

⚡ Quick Start (Local Development)

1. Clone repo

git clone https://github.com/<your-username>/smart-insights-dashboard.git
cd smart-insights-dashboard

2. Setup backend (FastAPI)

cd server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

Backend will run at http://127.0.0.1:8000.

3. Setup frontend (Next.js)

cd client
npm install
npm run dev

Frontend will run at http://localhost:3000.

4. Environment variables

Create .env files in server/ and client/:

server/.env

DATABASE_URL=postgresql://username:password@localhost:5432/sportsdb
JWT_SECRET=supersecretkey

client/.env

NEXT_PUBLIC_API_URL=http://127.0.0.1:8000


⸻

📊 Example API Routes

POST /api/auth/signup         # register user
POST /api/auth/login          # login & get JWT
GET  /api/users/{id}/favorites
GET  /api/data/player/{id}/stats
POST /api/predict             # return predicted performance
GET  /api/recommend           # personalized recommendations


⸻

📅 Roadmap (8–12 Weeks)
	•	Dataset prep + EDA
	•	Backend skeleton + DB schema
	•	Predictive ML model + API endpoint
	•	Dashboard with charts & filters
	•	User auth + saved favorites
	•	ML integration (recommendations/predictions in UI)
	•	Deployment (Vercel + Heroku/AWS)
	•	Polishing, docs, and demo video

⸻

🎥 Demo

(Add screenshots and a short 60–90s Loom/YouTube video link here once ready)

⸻

📖 Documentation
	•	FastAPI Docs (auto-generated)
	•	Full walkthrough in /docs folder
	•	GitHub Actions for CI/CD (coming soon)

⸻

👤 Author

Jonatan Filip Liljeblad
	•	🎓 CS & Math @ Albright College, Data Analytics minor
	•	💼 College athlete & golf coach → bridging sports + data + software
	•	🔗 LinkedIn | GitHub

⸻

⚖️ License

MIT License – free to use, modify, and share.

⸻
