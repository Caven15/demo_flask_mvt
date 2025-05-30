from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(200), nullable=False)
    