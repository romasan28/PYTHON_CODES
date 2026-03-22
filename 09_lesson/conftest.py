import pytest
from models import SessionLocal, Base, engine


@pytest.fixture(scope="function")
def db_session():
    """Фикстура, предоставляющая сессию БД с откатом после теста."""
    session = SessionLocal()
    try:
        yield session
        session.rollback()
    finally:
        session.close()


@pytest.fixture(scope="session", autouse=True)
def create_tables():
    """Создаёт таблицы перед тестами и удаляет после."""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
