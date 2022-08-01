from sqlalchemy import Column, String
from core.commons.base_enum import SexType
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from modules.users.models.detail_roll_call_model import DetailRollCall



class Student(Base):
    __tablename__ = 'students'
    name= Column(String(30),nullable=False)
    date_of_birth = Column(String(30))
    sex = Column(ENUM(SexType))
    course = Column(String(30))
    
    student_subject_classes = relationship('student_subject_classes', lazy="joined", back_populates="students")
    detail_roll_calls = relationship(DetailRollCall, lazy="joined", back_populates="students")
    