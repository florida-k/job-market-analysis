import requests

from dotenv import load_dotenv
import os

load_dotenv()

app_id = os.getenv("API_ID")
app_key = os.getenv("API_KEY")

country = "us"
page = 1

url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"

params = {
    "app_id": app_id,
    "app_key": app_key
}

response = requests.get(url, params=params)

#print(response.status_code)
#print(response.json())

data = response.json()

print(data.keys())
