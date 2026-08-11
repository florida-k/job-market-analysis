import pandas as pd
from api import get_jobs
import re


def average_salary(jobs):
    df = pd.DataFrame(jobs)

    salaries = df["salary"].dropna()

    if salaries.empty:
        return None

    return round(float(salaries.mean()), 2)


def top_locations(jobs, limit=5):
    df = pd.DataFrame(jobs)

    return df["location"].value_counts().head(limit)


def top_companies(jobs, limit=5):
    df = pd.DataFrame(jobs)

    return df["company"].value_counts().head(limit)

def top_skills(jobs, limit=10):
    skills = [
        "Python",
        "Java",
        "C++",
        "JavaScript",
        "TypeScript",
        "React",
        "Angular",
        "SQL",
        "AWS",
        "Azure",
        "Docker",
        "Kubernetes",
        "Git",
        "Excel",
        "Tableau",
        "Power BI"
    ]

    skill_counts = {}

    for skill in skills:
        count = 0

        for job in jobs:
            description = job.get("description") or ""

            pattern = rf"\b{re.escape(skill)}\b"

            if re.search(pattern, description, re.IGNORECASE):
                count += 1

        if count > 0:
            percentage = round((count / len(jobs)) * 100, 1)
            skill_counts[skill] = percentage

    sorted_skills = sorted(
        skill_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return dict(sorted_skills[:limit])


def analyze_market(search_job):
    jobs = get_jobs(search_job, pages=3)

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


if __name__ == "__main__":
    results = analyze_market("software engineer")
    print(results)

    results = analyze_market("data analyst")
    print(results)