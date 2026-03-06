"""
ArogyaMitra - FastAPI Main Application
Entry point for backend server
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from app.database.db import Base, engine
from app.core.settings import settings

# Import API Routers
from app.api import auth
from app.api import users
from app.api import workouts
from app.api import nutrition
from app.api import health
from app.api import ai_coach

# ---------------------------------------------------
# CREATE DATABASE TABLES
# ---------------------------------------------------

Base.metadata.create_all(bind=engine)

# ---------------------------------------------------
# FASTAPI APPLICATION
# ---------------------------------------------------

app = FastAPI(
    title="ArogyaMitra AI Healthcare Platform",
    description="AI Powered Workout, Nutrition Planner and Health Coach",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ---------------------------------------------------
# CORS MIDDLEWARE
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠ Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# STATIC FILES
# ---------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# ---------------------------------------------------
# INCLUDE API ROUTES
# ---------------------------------------------------

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    workouts.router,
    prefix="/workouts",
    tags=["Workouts"]
)

app.include_router(
    nutrition.router,
    prefix="/nutrition",
    tags=["Nutrition"]
)

app.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

app.include_router(
    ai_coach.router,
    prefix="/ai_coach",
    tags=["AI Coach"]
)

# ---------------------------------------------------
# ROOT ENDPOINT
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "project": "ArogyaMitra",
        "description": "AI Health Assistant",
        "status": "running",
        "documentation": "/docs"
    }

# ---------------------------------------------------
# SERVER HEALTH CHECK
# ---------------------------------------------------

@app.get("/ping")
def ping():
    return {
        "status": "healthy",
        "service": "ArogyaMitra Backend"
    }

# ---------------------------------------------------
# GLOBAL ERROR HANDLER
# ---------------------------------------------------

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal Server Error",
            "details": str(exc)
        }
    )
