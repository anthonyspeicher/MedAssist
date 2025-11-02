from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# create session and base
engine = create_engine("postgresql://meduser:medpass@localhost:5432/medassist")
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
