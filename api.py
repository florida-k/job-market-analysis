import requests
from dotenv import load_dotenv
import os

load_dotenv()

app_id = os.getenv("API_ID")
app_key = os.getenv("API_KEY")


def get_jobs(search_job):
    country = "us"
    page = 1

    print("API ID loaded:", bool(app_id))
    print("API KEY loaded:", bool(app_key))

    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "what": search_job
    }

    response = requests.get(url, params=params)

    print("Status code:", response.status_code)

    if response.status_code != 200:
        print("Adzuna request failed.")
        print(response.text[:500])
        return []

    data = response.json()

    all_jobs = []

    for job in data["results"]:
        job_data = {
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "salary": job.get("salary_min"),
            "created": job.get("created")
        }

        all_jobs.append(job_data)

    return all_jobs