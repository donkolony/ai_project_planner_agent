from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./plans.db"  # Local DB
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    """Create database tables"""
    from app.models.db_models import PlanDB

    SQLModel.metadata.create_all(engine)


def get_session():
    """Provide a session for API endpoints"""
    with Session(engine) as session:
        yield session
