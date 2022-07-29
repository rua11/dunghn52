from sqlalchemy import Column, ForeignKey, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID
from modules.users.models.subject_class_model import SubjectClass
from modules.users.models.teacher_model import Teacher


class RollCall(Base):
    __tablename__ = 'rollcalls'
    teacher_id = Column(UUID(as_uuid=True),ForeignKey(Teacher.id), nullable= False)
    subject_classes_id =  Column(UUID(as_uuid=True),ForeignKey(SubjectClass.id), nullable= False)
    semester = Column(String(30),nullable=False)
    year = Column(String(30),nullable=False)
    
