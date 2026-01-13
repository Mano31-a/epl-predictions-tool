"""
Database configuration and session management using SQLAlchemy async.

This module provides:
- Async engine and session factory setup
- Session dependency injection for FastAPI
- Database connection pooling
- Context managers for transaction handling
"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

# Database base class for all models
Base = declarative_base()

# Database configuration
DATABASE_URL = "sqlite+aiosqlite:///./epl_predictions.db"
# For production, use PostgreSQL:
# DATABASE_URL = "postgresql+asyncpg://user:password@localhost/epl_predictions"


class DatabaseConfig:
    """Configuration for database connection and pooling."""

    # Connection pool settings
    POOL_SIZE = 20  # Number of connections to keep in the pool
    MAX_OVERFLOW = 10  # Maximum overflow connections beyond pool_size
    POOL_PRE_PING = True  # Test connections before using them
    POOL_RECYCLE = 3600  # Recycle connections after 1 hour
    ECHO = False  # Set to True to log SQL statements


async def create_db_engine() -> AsyncEngine:
    """
    Create and configure the async database engine.

    Returns:
        AsyncEngine: Configured SQLAlchemy async engine
    """
    engine = create_async_engine(
        DATABASE_URL,
        echo=DatabaseConfig.ECHO,
        pool_pre_ping=DatabaseConfig.POOL_PRE_PING,
        pool_recycle=DatabaseConfig.POOL_RECYCLE,
        # For SQLite, use NullPool to avoid threading issues
        poolclass=NullPool if "sqlite" in DATABASE_URL else None,
    )
    return engine


# Create async session factory
async_engine = None
async_session_factory = None


async def init_db_engine() -> None:
    """Initialize the database engine and session factory."""
    global async_engine, async_session_factory

    async_engine = await create_db_engine()
    async_session_factory = sessionmaker(
        async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
        autocommit=False,
    )


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency injection function for FastAPI routes.

    Yields:
        AsyncSession: Database session for the request

    Example:
        @app.get("/teams")
        async def get_teams(db: AsyncSession = Depends(get_db)):
            result = await db.execute(select(Team))
            return result.scalars().all()
    """
    if async_session_factory is None:
        raise RuntimeError("Database not initialized. Call init_db_engine() first.")

    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()


async def create_tables() -> None:
    """
    Create all database tables from model definitions.

    Should be called once during application startup.
    """
    if async_engine is None:
        raise RuntimeError("Database engine not initialized. Call init_db_engine() first.")

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables() -> None:
    """
    Drop all database tables.

    WARNING: This will delete all data. Use only for development/testing.
    """
    if async_engine is None:
        raise RuntimeError("Database engine not initialized. Call init_db_engine() first.")

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def close_db_engine() -> None:
    """
    Close the database engine and dispose of all connections.

    Should be called during application shutdown.
    """
    global async_engine

    if async_engine:
        await async_engine.dispose()
        async_engine = None


class AsyncSessionManager:
    """Context manager for managing async database sessions."""

    def __init__(self, session_factory):
        """
        Initialize the session manager.

        Args:
            session_factory: SQLAlchemy async session factory
        """
        self.session_factory = session_factory

    async def __aenter__(self) -> AsyncSession:
        """Enter the async context and return a session."""
        self.session = self.session_factory()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit the async context and close the session."""
        await self.session.close()


async def get_session() -> AsyncSession:
    """
    Create and return a new async session.

    Returns:
        AsyncSession: A new database session

    Example:
        session = await get_session()
        try:
            # Use session
        finally:
            await session.close()
    """
    if async_session_factory is None:
        raise RuntimeError("Database not initialized. Call init_db_engine() first.")
    return async_session_factory()
