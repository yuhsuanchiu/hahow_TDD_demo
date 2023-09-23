import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import Base


@pytest.fixture(name='sqlite_session')
def sqlite_session_fixture() -> Session:
    engine_url = 'sqlite://'
    engine = create_engine(engine_url)

    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        yield session

    Base.metadata.drop_all(engine)
