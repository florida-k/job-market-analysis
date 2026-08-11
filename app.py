from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from analysis import analyze_market

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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