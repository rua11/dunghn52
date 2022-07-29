from sqlalchemy import Column, ForeignKey, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID
from modules.users.models.work_unit_model import WorkUnit
from sqlalchemy.orm import relationship



class Teacher(Base):
    __tablename__ = 'teachers'
    name = Column(String(30),nullable=False)
    level = Column(String(10),nullable=False)
    specialize = Column(String(50),nullable=False)
    workunit_id = Column(UUID(as_uuid=True),ForeignKey(WorkUnit.id), nullable= False)
    
    workunit = relationship(WorkUnit, lazy="joined", back_populates="teachers")
    subject_classes = relationship('subjectclasses', lazy='joined', back_populates='teachers')
    