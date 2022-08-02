from sqlalchemy import Column, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.orm import relationship



class ClassRoom(Base):
    __tablename__ = 'class_rooms'
    name = Column(String(30),nullable=False)
    address =Column(String(50))
    slot = Column(Integer,nullable=False) 
    
    lesson_clroom_subject_cls = relationship('LessonClroomSubjectCl', lazy='joined', back_populates='class_rooms')
    