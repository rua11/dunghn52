from sqlalchemy import Column, ForeignKey,  String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID
from modules.users.models.student_model import Student
from modules.users.models.subject_class_model import SubjectClass


class StudentSubjectClass(Base):
    __tablename__ = 'student_subject_classes'
    subject_classes_id = Column(UUID(as_uuid=True),ForeignKey(SubjectClass.id), nullable= False)
    student_id =  Column(UUID(as_uuid=True),ForeignKey(Student.id), nullable= False)
    semester = Column(String(30),nullable=False)
    year = Column(String(30),nullable=False)
    