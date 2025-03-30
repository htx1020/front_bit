from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Mcap(Base):
    __tablename__ = 'mcap'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    start_time = Column(DateTime, nullable=False)
    file_size = Column(Float)
    insert_time = Column(DateTime, default=datetime.utcnow)
    note = Column(String(500))


class Frame(Base):
    __tablename__ = 'frame'
    
    id = Column(Integer, primary_key=True)
    mcap_id = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    oss_info = Column(String(500))
    insert_time = Column(DateTime, default=datetime.utcnow)
