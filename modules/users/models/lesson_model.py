from sqlalchemy import Column, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.orm import relationship


class Lesson(Base):
    __tablename__ = 'lessons'
    starttime = Column(String(30),nullable=False)
    endtime =Column(String(50),nullable=False)
    number_of_sessions = Column(Integer)
    
    lesson_clroom_subject_cls = relationship('lesson_clroom_subject_cl', lazy='joined', back_populates='lessons')
    
    