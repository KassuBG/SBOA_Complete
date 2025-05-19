
from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics")
def dashboard_metrics():
    return {
        "leads": 120,
        "active_users": 34,
        "revenue": 5600
    }
