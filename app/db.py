from sqlmodel import SQLModel, create_engine

from app.config import settings

engine = create_engine(settings.DATABASE_URL,
                      connect_args={"check_same_thread": False})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)

