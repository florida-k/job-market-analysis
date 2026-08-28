import pandas as pd
from api import get_jobs
import re
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
    skills = [
        "Python", "Java", "C++", "C Programming", "JavaScript", "TypeScript",
        "React", "Node.js", "HTML", "CSS", "SQL", "MySQL",
        "PostgreSQL", "MongoDB", "Git", "GitHub", "Linux",
        "Docker", "Kubernetes", "AWS", "Azure", "GCP",
        "FastAPI", "Django", "Flask", "Pandas", "NumPy",
        "Matplotlib", "TensorFlow", "PyTorch", "Machine Learning",
        "Data Analysis", "Data Science", "Power BI", "Tableau",
        "Excel", "R Programming", "Spark", "Hadoop", "REST API",
        "Agile", "Scrum", "Jira", "Salesforce", "QuickBooks",
        "Accounting", "Marketing", "SEO", "Customer Service",
        "Project Management", "Communication","Leadership","Problem Solving",
        "Critical Thinking","Time Management","Teamwork","Public Speaking","Negotiation",
        "Research","Technical Writing","Documentation","Customer Support",
        "Customer Relations","Client Management","Business Analysis","Business Intelligence",
        "Business Development","Operations Management","Data Entry",
        "Data Visualization","Statistics","ETL","Data Warehousing",
        "Big Data","Predictive Modeling","Artificial Intelligence",
        "Deep Learning","Computer Vision","Natural Language Processing",
        "NLP","Generative AI","LLM","OpenAI","PHP","Ruby","Ruby on Rails",
        "Go","Golang","Rust","Swift","Kotlin","",".NET","Spring Boot",
        "Angular","Vue","Next.js","Express.js","Bootstrap","Tailwind CSS",
        "GraphQL","API Development","Microservices","CI/CD","Jenkins",
        "Terraform","Ansible","Cybersecurity","Network Security","Penetration Testing",
        "Incident Response","Risk Management","Compliance","Computer Networking",
        "TCP/IP","Active Directory","Windows Server","AutoCAD",
        "SolidWorks","MATLAB","Simulink","Embedded Systems","ROS",
        "Healthcare","Nursing","Patient Care","Epic","Cerner",
        "Medical Records","Clinical Research","Finance","Financial Analysis","Financial Modeling",
        "Auditing","Bookkeeping","Tax Preparation","Recruiting",
        "Talent Acquisition","Human Resources","HRIS",
        "Supply Chain","Inventory Management","Procurement","Logistics",
        "Digital Marketing","Content Creation","Social Media Marketing","Google Analytics",
        "Google Ads","Email Marketing","Teaching","Curriculum Development",
        "Tutoring","Lesson Planning"
    ]
    skillcounts = {}

    for skill in skills:
        count =0

        for job in jobs:
            description = (job.get("description") or "").lower()

            if skill.lower() in description:
                count+=1

        if count >0:

            percentage = round((count / len(jobs)) *100,1)
            skillcounts[skill] = percentage


    sortedskills = sorted(
        skillcounts.items(),
        key=lambda x:x[1],
        reverse=True
    )
    return dict(sortedskills[:limit])


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

