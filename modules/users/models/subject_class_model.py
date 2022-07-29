from sqlalchemy import Column, ForeignKey, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID
from modules.users.models.teacher_model import Teacher
from sqlalchemy.orm import relationship


class SubjectClass(Base):
    __tablename__ = 'subject_classes'
    name = Column(String(30),nullable=False)
    teacher_id = Column(UUID(as_uuid=True),ForeignKey(Teacher.id), nullable= False)
    
    teachers = relationship('teachers', lazy='joined', back_populates='subject_classes')