import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_api_url():
    return os.getenv("OMQS_API_URL", "https://om-qs.com/api/v1/models/")

class OMQSClient:
    def __init__(self, **options):
        self.api_key = options.get("api_key", os.getenv("OMQS_API_KEY"))
        self.api_url = options.get("api_url", get_api_url())
        self.headers = {
            "Authorization": f"Api-Key {self.api_key}"
        }

    def get_signal(self, model: str, ticker: str, timeframe: str):
        payload = {
            "model": model,
            "ticker": ticker,
            "timeframe": timeframe
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"[OMQS ERROR {response.status_code}] {response.text}")
                return None
        except requests.exceptions.ConnectionError:
            print(f"[OMQS ERROR] Connection error. Is the server running at {self.api_url}?")
        except requests.exceptions.RequestException as e:
            print(f"[OMQS ERROR] Request exception: {e}")
