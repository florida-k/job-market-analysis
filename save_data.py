from api import get_jobs
import csv

jobs = get_jobs("software engineer")

with open("jobs.csv","w",newline = "") as file:
    writer = csv.DictWriter(file,fieldnames = jobs[0].keys())
    writer.writeheader()
    writer.writerows(jobs)

print("Jobs saved successfully!")