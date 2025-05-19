
from utils.forecasting import forecast_sales

def generate_insights(data):
    forecast = forecast_sales(data)
    return {"forecast": forecast}
