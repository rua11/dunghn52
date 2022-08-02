from sqlalchemy import Column, ForeignKey, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID
from modules.users.models.subject_class_model import SubjectClass
from modules.users.models.teacher_model import Teacher
from sqlalchemy.orm import relationship



class RollCall(Base):
    __tablename__ = 'roll_calls'
    teacher_id = Column(UUID(as_uuid=True),ForeignKey(Teacher.id), nullable= False)
    subject_classes_id =  Column(UUID(as_uuid=True),ForeignKey(SubjectClass.id), nullable= False)
    semester = Column(String(30))
    year = Column(String(30))
    
    teachers = relationship(Teacher, lazy= 'joined',back_populates= 'roll_calls')
    subject_classes = relationship(SubjectClass, lazy= 'joined',back_populates= 'roll_calls')
    
    detail_roll_calls = relationship('DetailRollCall', lazy="joined", back_populates="roll_calls")
    
    
