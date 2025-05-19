
import os
from dotenv import load_dotenv
load_dotenv()
def get_settings():
    return {
        "stripe_key": os.getenv("STRIPE_SECRET_KEY", "test_key")
    }

