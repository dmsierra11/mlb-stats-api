"""Main application module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import mlb_router

app = FastAPI(
    title="MLB Stats API",
    description="A FastAPI service for fetching MLB statistics",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    mlb_router.router,
    prefix="/api/v1",
)


@app.get("/")
async def root() -> dict[str, str]:
    """Return a welcome message."""
    return {"message": "Welcome to MLB Stats API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
