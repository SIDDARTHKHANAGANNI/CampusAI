from fastapi import FastAPI

app = FastAPI(
    title="CampusAI API",
    description="Backend API for CampusAI Student Success & Career Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CampusAI API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }