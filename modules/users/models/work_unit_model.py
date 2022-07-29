from sqlalchemy import Column, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.orm import relationship



class WorkUnit(Base):
    __tablename__ = 'workunits'
    name = Column(String(30),nullable=False)
    
    workunit = relationship('teachers', lazy="joined", back_populates="workunit")
    
