"""Main application module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import example_router

app = FastAPI(
    title="FastAPI Microservice Template",
    description="A template for building microservices with FastAPI",
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
    example_router.router,
    prefix="/api/v1",
)


@app.get("/")
async def root() -> dict[str, str]:
    """Return a welcome message."""
    return {"message": "Welcome to FastAPI Microservice Template"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
