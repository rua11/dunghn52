from modules.users.models.roll_call_model import RollCall
from sqlalchemy import Column, ForeignKey, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class DetailRollCall(Base):
    __tablename__ = 'detail_roll_calls'
    roll_call_id = Column(UUID(as_uuid=True),ForeignKey(RollCall.id), nullable= False)
    student_id =  Column(UUID(as_uuid=True),ForeignKey('students.id'), nullable= False)
    absent = Column(Integer)
    reason = Column(String(200))
    
    students = relationship('Student', lazy="joined", back_populates="detail_roll_calls")
    roll_calls = relationship(RollCall, lazy="joined", back_populates="detail_roll_calls")
    
    