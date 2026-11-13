import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Создание базового класса для моделей SQLAlchemy
Base = declarative_base()

# URL базы данных
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///movies.db")

# Создание движка SQLAlchemy для подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создание базового класса для моделей SQLAlchemy
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

# Предоставление сессии базе данных для обработки запроса
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()