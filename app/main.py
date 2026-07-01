from fastapi import FastAPI
from app.api.osint import router as osint_router
from app.api.history import router as history_router
from app.core.config import settings
from app.core.logger import logger
from app.core.exceptions import global_exception_handler
from app.core.middleware import LoggingMiddleware

from app.database.database import engine
from app.database.database import Base

import app.models

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

Base.metadata.create_all(bind=engine)

app.add_middleware(LoggingMiddleware)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(osint_router)
app.include_router(history_router)

logger.info("Advanced Website OSINT Framework Started")

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