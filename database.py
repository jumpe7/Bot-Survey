import os

from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker)
from models import Base

from dotenv import load_dotenv
load_dotenv()
PG_URL = os.getenv("DB_URL")

engine = create_async_engine(PG_URL, connect_args={"ssl": "require"})

Session = async_sessionmaker(engine, expire_on_commit=False)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)