from sqlalchemy import Column, ForeignKey, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from modules.users.models.subject import Subject
from modules.users.models.subject_class_model import SubjectClass


class SubjectSubjectClass(Base):
    __tablename__ = 'subjec_subject_classes'
    subject_id = Column(UUID(as_uuid=True),ForeignKey(Subject.id), nullable= False)
    semester = Column(String(30))
    year = Column(String(30))
    subject_class_id = Column(UUID(as_uuid=True),ForeignKey(SubjectClass.id), nullable= False)
    number_of_students = Column(Integer)
    
    subjects = relationship(Subject, lazy='joined', back_populates='subject_subject_classes')
    subject_classes = relationship(SubjectClass, lazy='joined', back_populates='subject_subject_classes')
    