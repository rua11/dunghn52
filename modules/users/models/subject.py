from sqlalchemy import Column, Integer, String
from core.commons.base_model import BaseModel as Base


class Subject(Base):
    __tablename__ = 'subjects'
    name = Column(String(30),nullable=False)
    totallesson = Column(Integer)
    theory = Column(Integer)
    practice = Column(Integer)