import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://aiuser:ai_pass_123@localhost:5432/aiinvoice")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):
    pass

def init_db():
    # temp create_all for bootstrapping; replace with Alembic later
    from . import models
    Base.metadata.create_all(bind=engine)