# Smart Business Operations Assistant (SBOA)

A full-stack AI-powered web application to help businesses manage operations intelligently using cooperative AI Agents.

---

## 🌐 Live Preview
Once running locally, access the app at:

- **Frontend**: `http://localhost:3000`
- **Backend (FastAPI)**: `http://127.0.0.1:8000`

---

## 📁 Project Structure

```plaintext
SBOA_Complete/
├── sboa/
│   ├── frontend/            # React frontend app
│   │   ├── public/
│   │   └── src/
│   │       └── components/  # React components for UI
│   └── backend/             # FastAPI backend app (main.py)
├── README.md
└── .gitignore
```

---

## 🧠 Features

- 🔄 **Cooperative AI Agents** for task automation
- 🧾 **Smart Dashboard** showing active metrics
- 📤 Realtime communication with backend
- 💡 FastAPI backend with agent integration
- ⚛️ Clean React interface with modular components

---

## ⚙️ Requirements

- **Python** >= 3.8
- **Node.js** = 18.x (not higher!)
- **npm** >= 7

---

## 🚀 Setup Instructions

### 🔧 Backend (FastAPI)

```bash
cd sboa/backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### 🖥️ Frontend (React)

> ⚠️ Ensure you are using Node 18.x. If `nvm` isn't installed:
> 
> **Mac/Linux**:
> ```bash
> curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
> source ~/.bashrc  # or ~/.zshrc
> nvm install 18
> nvm use 18
> ```

```bash
cd sboa/frontend
rm -rf node_modules package-lock.json
npm install
npm start
```

---

## 🐳 Docker Support (Optional)

Coming soon...

---

## 🔒 Security & Vulnerabilities

- Use `npm audit fix` to patch common vulnerabilities
- Recommended: Add `.env` and `.env.local` for sensitive configs (not in repo)

---

## ☁️ Deployment (Optional)

Coming soon with full GitHub Actions + CI/CD + Docker support

---

## 👨‍💻 Contributors

- Kas Gebresellasie — [GitHub](https://github.com/KassuBG) — kas@xodusai.com

---

## 📄 License

MIT License © 2025 Kas Gebresellasie

---

## 📌 Notes

If you encounter:

- `ERR_OSSL_EVP_UNSUPPORTED` — Use Node.js v18, not v23+.
- `npm start` missing: Ensure `package.json` in `frontend/` includes:

```json
"scripts": {
  "start": "react-scripts start"
}
```

---

Happy Hacking! 🚀

