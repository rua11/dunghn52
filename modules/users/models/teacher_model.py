from sqlalchemy import Column, ForeignKey, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID
from modules.users.models.work_unit_model import WorkUnit
from sqlalchemy.orm import relationship



class Teacher(Base):
    __tablename__ = 'teachers'
    name = Column(String(30),nullable=False)
    level = Column(String(10))
    specialize = Column(String(50))
    work_unit_id = Column(UUID(as_uuid=True),ForeignKey(WorkUnit.id), nullable= False)
    
    work_unit = relationship(WorkUnit, lazy="joined", back_populates="teachers")
    subject_classes = relationship('SubjectClass', lazy='joined', back_populates='teachers')
    roll_calls = relationship('RollCall', lazy='joined', back_populates='teachers')
    