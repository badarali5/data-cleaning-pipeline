from fastapi import FastAPI

from app.controller.patient_routes import router as patient_router

app = FastAPI(
    title="Healthcare API",
    description="FastAPI for healthcare dataset",
    version="1.0.0"
)

app.include_router(patient_router)


@app.get("/")
def root():
    return {
        "message": "Healthcare API is running"
    }