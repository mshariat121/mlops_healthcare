from fastapi import FastAPI

from api.routers import risk
from api.routers import claim

app = FastAPI(title="HealthCare ML API")

@app.get("/")
def root():
    return {"message": "HealthCare ML API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(risk.router, prefix= "/predict", tags = ["Risk Score prediction"])
app.include_router(claim.router, prefix= "/predict", tags = ["Claim Status prediction"])