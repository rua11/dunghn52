from sqlalchemy import Column, Integer, String
from core.commons.base_model import BaseModel as Base


class ClassRoom(Base):
    __tablename__ = 'classrooms'
    name = Column(String(30),nullable=False)
    address =Column(String(50),nullable=False)
    slot = Column(Integer,nullable=False) 
    slot2 = Column(Integer,nullable=False) 