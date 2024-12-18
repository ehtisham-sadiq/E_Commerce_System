from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from .config import database_url
from typing import AsyncGenerator

async_database_url = database_url.replace("postgresql://", "postgresql+asyncpg://")
engine = create_async_engine(async_database_url, echo=True)

database = Database(async_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

