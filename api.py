import requests
from dotenv import load_dotenv
import os


env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

app_id = os.getenv("API_ID")
app_key = os.getenv("API_KEY")


def get_jobs(search_job, pages=5):
    country = "us"
    all_jobs = []

    for page in range(1, pages + 1):

        url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"

        params = {
            "app_id": app_id,
            "app_key": app_key,
            "what": search_job
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print("Adzuna request failed.")
            print("Status code:", response.status_code)
            continue

        data = response.json()
        print(data)

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