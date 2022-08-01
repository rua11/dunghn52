from sqlalchemy import Column, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.orm import relationship



class WorkUnit(Base):
    __tablename__ = 'work_units'
    name = Column(String(30),nullable=False)
    
    work_unit = relationship('teachers', lazy="joined", back_populates="work_unit")
    
