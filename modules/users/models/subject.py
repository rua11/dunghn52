from sqlalchemy import Column, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.orm import relationship



class Subject(Base):
    __tablename__ = 'subjects'
    name = Column(String(30),nullable=False)
    total_lesson = Column(Integer)
    theory = Column(Integer)
    practice = Column(Integer)
    
    subject_subject_classes = relationship('subjec_subject_classes', lazy='joined', back_populates='subjects')