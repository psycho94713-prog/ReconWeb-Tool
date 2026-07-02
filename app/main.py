from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.osint import router as osint_router
from app.api.history import router as history_router
from app.api.auth import router as auth_router
from app.routes.web import router as web_router

from app.core.config import settings
from app.core.logger import logger
from app.core.exceptions import global_exception_handler
from app.core.middleware import LoggingMiddleware

from app.database.database import engine, Base

import app.models

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

# Database
Base.metadata.create_all(bind=engine)

# Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Middleware
app.add_middleware(LoggingMiddleware)
app.add_exception_handler(Exception, global_exception_handler)

# Routers
app.include_router(web_router)
app.include_router(auth_router)
app.include_router(osint_router)
app.include_router(history_router)

logger.info("Advanced Website OSINT Framework Started")


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }