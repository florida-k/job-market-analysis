import pandas as pd
from api import get_jobs
import re
from keybert import KeyBERT
import matplotlib.pyplot as plt


def average_salary(jobs):
    df = pd.DataFrame(jobs) # make table of the list from api.py

    salaries = df["salary"].dropna() # drop salaries  with no number

    if salaries.empty:
        return None

    return round(float(salaries.mean()), 2) #


def top_locations(jobs, limit=5):
    df = pd.DataFrame(jobs)

    return df["location"].value_counts().head(limit) # returns th e top limit of repeated location


def top_companies(jobs, limit=5):
    df = pd.DataFrame(jobs)

    return df["company"].value_counts().head(limit) # returns th e top limit of repeated top companies

def top_skills(jobs, limit=10):
    all_text = ""

    for job in jobs:
        all_text += (job.get("description") or "") + " "

    if not all_text.strip():
        return {}

    kw_model = KeyBERT()

    keywords = kw_model.extract_keywords(
        all_text,
        keyphrase_ngram_range=(1,2),
        stop_words = "english",
        top_n=limit
    )

    return dict(keywords)


def analyze_market(search_job):
    jobs = get_jobs(search_job, pages=5)

    if not jobs:
        return None

    return {
        "job": search_job,
        "job_count": len(jobs),
        "average_salary": average_salary(jobs),
        "top_locations": top_locations(jobs).to_dict(),
        "top_companies": top_companies(jobs).to_dict(),
        "top_skills": top_skills(jobs)
    }

def companychart(jobs):
    companies = top_companies(jobs)

    companies.plot(kind="bar")

    plt.title("Top companies")
    plt.xlabel("Company")
    plt.ylabel("Jobs")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    pass
    #results = analyze_market("software engineer")
    #print(results)

    #results = analyze_market("data analyst")
    #print(results)

