"""Main FastAPI application."""

from fastapi import FastAPI

from app.routers import mlb_router

app = FastAPI(
    title="MLB Stats API",
    description="API for accessing MLB statistics and information",
    version="1.0.0",
)

app.include_router(mlb_router.router)
