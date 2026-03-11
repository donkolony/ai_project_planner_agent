import pytest
from sqlmodel import SQLModel, Session, create_engine
from app.main import app

# In-memory SQLite for testing
TEST_SQLITE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_SQLITE_URL, echo=False)

# Create tables before tests and drop afterwards
@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(scope="function", autouse=True)
def clean_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

# Fixture to provide a session for tests
@pytest.fixture()
def get_test_session():
    with Session(engine) as session:
        yield session

def get_test_session_override():
    with Session(engine) as session:
        yield session
