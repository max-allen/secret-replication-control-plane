from fastapi import FastAPI

from .database import ping_database

app = FastAPI(title="Multi-Region Secrets Control Plane")


@app.on_event("startup")
def startup():
    """Verify the database is reachable"""
    ping_database()


@app.get("/health")
def health_check():
    """Indicates service is running"""
    return {"status": "ok"}
