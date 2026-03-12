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
    """Create database tables"""
    from app.models.db_models import PlanDB

    SQLModel.metadata.create_all(engine)


def get_session():
    """Provide a session for API endpoints"""
    with Session(engine) as session:
        yield session
