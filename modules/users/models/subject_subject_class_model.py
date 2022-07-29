from sqlalchemy import Column, ForeignKey, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID

from modules.users.models.subject import Subject
from modules.users.models.subject_class_model import SubjectClass


class SubjectSubjectClass(Base):
    __tablename__ = 'subjec_subject_classes'
    subject_id = Column(UUID(as_uuid=True),ForeignKey(Subject.id), nullable= False)
    semester = Column(String(30),nullable=False)
    year = Column(String(30),nullable=False)
    subjectclass_id = Column(UUID(as_uuid=True),ForeignKey(SubjectClass.id), nullable= False)
    numberofstudents = Column(Integer)