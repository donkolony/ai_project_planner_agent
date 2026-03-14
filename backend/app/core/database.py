import os
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import get_settings
import logging

logger = logging.getLogger(__name__)

settings = get_settings()

# Ensure we have an absolute path for SQLite on Azure
DATABASE_URL = settings.database_url
if DATABASE_URL.startswith("sqlite"):
    # Extract the database path
    db_path = DATABASE_URL.replace("sqlite:///", "")
    if not os.path.isabs(db_path):
        # Make it absolute relative to the app's parent directory
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # Strip ./ if present
        db_path = db_path.lstrip("./")
        DATABASE_URL = f"sqlite:///{os.path.join(root_dir, db_path)}"
        logger.info(f"🗄️ Normalized Database URL: {DATABASE_URL}")

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
    logger.info("🛠️ Creating tables on engine metadata...")
    SQLModel.metadata.create_all(engine)
    
    # Log tables for verification
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    logger.info(f"📊 Registered tables in DB: {tables}")


def get_session():
    """Provide a session for API endpoints"""
    with Session(engine) as session:
        yield session
