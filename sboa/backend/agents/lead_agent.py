
def capture_leads(data):
    score = 0
    if data.get("email") and data.get("interaction_count", 0) > 2:
        score = 90
    return {"lead_score": score, "details": data}
