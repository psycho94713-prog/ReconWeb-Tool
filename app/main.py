from fastapi import FastAPI
from app.api.osint import router as osint_router

app = FastAPI(
    title="Advanced Website OSINT Framework",
    version="1.0.0",
)

app.include_router(osint_router)


@app.get("/")
async def root():
    return {
        "message": "Advanced Website OSINT Framework Running",
        "status": "success"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }