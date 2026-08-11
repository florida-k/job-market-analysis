import pandas as pd
from api import get_jobs


def average_salary(jobs):
    df = pd.DataFrame(jobs)

    salaries = df["salary"].dropna()

    if salaries.empty:
        return None

    return salaries.mean()


def top_locations(jobs, limit=5):
    df = pd.DataFrame(jobs)

    return df["location"].value_counts().head(limit)


def top_companies(jobs, limit=5):
    df = pd.DataFrame(jobs)

    return df["company"].value_counts().head(limit)


jobs = get_jobs("software engineer")

print("Average Salary:")
print(average_salary(jobs))

print("\nTop Locations:")
print(top_locations(jobs))

print("\nTop Companies:")
print(top_companies(jobs))