from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import billing, agents, dashboard

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(billing.router, prefix="/billing")
app.include_router(agents.router, prefix="/agents")
app.include_router(dashboard.router, prefix="/dashboard")

@app.get("/")
def root():
    return {"message": "Welcome to Smart Business Operations Assistant (SBOA) API"}