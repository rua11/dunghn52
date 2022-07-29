from sqlalchemy import Column, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.orm import relationship


class Lesson(Base):
    __tablename__ = 'lessons'
    starttime = Column(String(30),nullable=False)
    endtime =Column(String(50),nullable=False)
    numberofsessions = Column(Integer)
    
    