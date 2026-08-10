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
    "app_key": app_key,
    "what": "software engineer"
}

response = requests.get(url, params=params)

#print(response.status_code)
#print(response.json())

data = response.json()

#print(data["results"][0])

alljobs = []

for job in data["results"]:
    title = job["title"]
    company = job["company"]["display_name"]
    location = job["location"]["display_name"]
    description = job["description"]
    salary = job["salary_min"]
    created = job["created"]

    job_data = {
        "title": title,
        "company": company,
        "location": location,
        "description": description,
        "salary": salary,
        "created": created
    }
    alljobs.append(job_data)

    #print(title)
    #print(company)
    #print(location)
    #print(description)
    #print(salary_min)
    #print(created)
    #print()

print(len(alljobs))
print(alljobs[0])