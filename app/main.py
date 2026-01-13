"""
Main FastAPI application module for EPL Predictions Tool.
Handles application initialization, database setup, CORS configuration, and route mounting.
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import init_db, get_db
from app.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """
    Manage application lifecycle events.
    
    Startup: Initialize database
    Shutdown: Cleanup resources
    """
    # Startup
    print("Starting up EPL Predictions Tool...")
    await init_db()
    print("Database initialized successfully")
    
    yield
    
    # Shutdown
    print("Shutting down EPL Predictions Tool...")


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="API for EPL match predictions using machine learning",
        version=settings.API_VERSION,
        lifespan=lifespan,
    )
    
    # Configure CORS
    _configure_cors(app)
    
    # Mount API routes
    _mount_routes(app)
    
    # Add health check endpoint
    _add_health_check(app)
    
    return app


def _configure_cors(app: FastAPI) -> None:
    """
    Configure CORS middleware for the application.
    
    Args:
        app: FastAPI application instance
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )


def _mount_routes(app: FastAPI) -> None:
    """
    Mount API routers to the application.
    
    Args:
        app: FastAPI application instance
    """
    app.include_router(api_router, prefix="/api/v1")


def _add_health_check(app: FastAPI) -> None:
    """
    Add health check endpoint.
    
    Args:
        app: FastAPI application instance
    """
    @app.get("/health", tags=["Health"])
    async def health_check():
        """Health check endpoint"""
        return {
            "status": "healthy",
            "service": settings.PROJECT_NAME,
            "version": settings.API_VERSION,
        }


# Create the FastAPI application instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )
