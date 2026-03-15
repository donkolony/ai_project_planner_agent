"""
Database configuration and session management.

Sets up the SQLModel database engine, dynamically configuring connection pooling
and arguments based on whether the environment is using a local SQLite database
or a production SQL Server (Azure SQL) instance.
"""

from sqlmodel import SQLModel, create_engine, Session
from app.core.config import get_settings

settings = get_settings()

# Use database URL from settings (supports SQLite locally, SQL Server in Azure)
DATABASE_URL = settings.database_url

# Additional engine options for production
engine_kwargs = {}
if DATABASE_URL.startswith("mssql"):
    # SQL Server specific options
    engine_kwargs = {
        "echo": settings.debug,
        "pool_pre_ping": True,
        "pool_recycle": 3600,
    }
else:
    # SQLite options
    engine_kwargs = {"echo": settings.debug}

engine = create_engine(DATABASE_URL, **engine_kwargs)


def init_db():
    """
    Initialize the database by creating all defined tables.

    Binds the SQLModel metadata to the engine and creates the tables in the database
    if they do not already exist. Imports models locally inside the function
    to prevent circular import errors during app startup.
    """
    from app.models.db_models import PlanDB

    SQLModel.metadata.create_all(engine)


def get_session():
    """
    Provide a transactional database session for FastAPI endpoints.

    Designed to be used as a FastAPI dependency (`Depends(get_session)`).
    Yields a SQLModel Session object and automatically closes it when the
    request context ends to prevent connection leaks.

    Yields:
        Session: A SQLModel database session instance.
    """
    with Session(engine) as session:
        yield session
