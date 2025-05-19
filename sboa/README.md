# SBOA: Smart Business Operations Assistant

SBOA is a full-stack AI-driven platform designed to enhance operational efficiency, decision-making, and business intelligence through a responsive frontend, FastAPI backend, and modular agents.

---

## 🔧 Project Structure

```
SBOA_Complete/
├── sboa/
│   ├── backend/              # FastAPI backend
│   │   ├── main.py           # Entry point for API
│   │   └── ...
│   ├── frontend/             # React-based frontend
│   │   ├── public/
│   │   │   └── index.html
│   │   ├── src/
│   │   │   └── App.js        # Main React component
│   │   └── package.json
│   └── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Features

- 🌐 **Frontend (React)**
  - Dynamic UI for real-time dashboard
  - Visualizes key business metrics
  - Fully responsive and interactive

- ⚙️ **Backend (FastAPI)**
  - RESTful API endpoints
  - Serves business logic and data
  - Ready for agent-based extension

- 🤖 **AI Agents (Planned)**
  - Integrate intelligent modules for prediction, recommendation, and anomaly detection

---

## 🧪 Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/KassuBG/SBOA_Complete.git
cd SBOA_Complete
```

### 2. Backend Setup (Python)

```bash
cd sboa/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

- Server runs at: `http://127.0.0.1:8000`

### 3. Frontend Setup (React)

```bash
cd ../frontend
nvm install 18
nvm use 18
rm -rf node_modules package-lock.json
npm install
npm start
```

- App runs at: `http://localhost:3000`

> ⚠️ If you get OpenSSL errors, downgrade Node.js to v18 using `nvm` as shown.

---

## 📦 Deployment

- Docker/Kubernetes-ready (in progress)
- Planned CI/CD via GitHub Actions

---

## 📁 .gitignore Suggestions

```
node_modules
venv
__pycache__
.env
.DS_Store
*.log
```

---

## 📍 License
MIT

---

## 📬 Contact
**Author:** Kassu G.  
**GitHub:** [KassuBG](https://github.com/KassuBG)

---

Feel free to fork, contribute, and suggest enhancements!



