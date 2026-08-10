import requests

from dotenv import load_dotenv
import os

load_dotenv()

app_id = os.getenv("API_ID")
app_key = os.getenv("API_KEY")

#writing function that requests from adzuna and stores in a list and returns

def get_jobs(search_job):
    country = "us"
    page = 1

    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"

    params = {
        "app_id" : app_id,
        "app_key": app_key,
        "what": search_job
    }

    response = requests.get(url,params = params)
    data = response.json()

    all_jobs = []

####adds all the jobs in from the search into a list so we can do what we want with it
    for job in data["results"]:
        job_data = {
            "title": job["title"],
            "company": job["company"]["display_name"],
            "location": job["location"]["display_name"],
            "description": job["description"],
            "salary": job["salary_min"],
            "created": job["created"]
        }

        all_jobs.append(job_data)

    return all_jobs