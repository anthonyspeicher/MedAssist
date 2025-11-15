from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import os

# create session and base
DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL)
localSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# base table structure
class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True)
    result = Column(String)
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
