from sqlalchemy import Column, String
from core.commons.base_enum import SexType
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import ENUM


class Student(Base):
    __tablename__ = 'students'
    name= Column(String(30),nullable=False)
    dateofbirth = Column(String(30),nullable=False)
    sex = Column(ENUM(SexType),nullable=False)
    course = Column(String(30),nullable=False)
    