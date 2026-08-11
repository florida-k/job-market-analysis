from fastapi import FastAPI
from analysis import analyze_market

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Job Market Analysis API"
    }


@app.get("/analysis")
def market_analysis(job: str):
    results = analyze_market(job)

    if results is None:
        return {
            "error": "No jobs found"
        }

    return results