from sqlalchemy import Column, ForeignKey, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID
from modules.users.models.classroom_model import ClassRoom
from modules.users.models.lesson_model import Lesson
from modules.users.models.subject_class_model import SubjectClass
from sqlalchemy.orm import relationship


class LessonClroomSubjectCl(Base):
    __tablename__ = 'lessonclroomsubjectcl'
    lesson_id = Column(UUID(as_uuid=True),ForeignKey(Lesson.id), nullable= False)
    classroom_id = Column(UUID(as_uuid=True),ForeignKey(ClassRoom.id), nullable= False)
    subject_class_id = Column(UUID(as_uuid=True),ForeignKey(SubjectClass.id), nullable= False)
    day_of_theweek = Column(String(30),nullable=False)
    
    lessons = relationship(Lesson, lazy='joined', back_populates='lessonclroomsubjectcls')
    classrooms = relationship(ClassRoom, lazy='joined', back_populates='lessonclroomsubjectcls')
    subject_classes = relationship(SubjectClass, lazy='joined', back_populates='lessonclroomsubjectcls')
    
    
    