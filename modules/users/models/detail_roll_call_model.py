from modules.users.models.roll_call_model import RollCall
from modules.users.models.student_model import Student
from sqlalchemy import Column, ForeignKey, Integer, String
from core.commons.base_model import BaseModel as Base
from sqlalchemy.dialects.postgresql import UUID

class DetailRollCall(Base):
    __tablename__ = 'detailrollcalls'
    rollcall_id = Column(UUID(as_uuid=True),ForeignKey(RollCall.id), nullable= False)
    student_id =  Column(UUID(as_uuid=True),ForeignKey(Student.id), nullable= False)
    absent = Column(Integer)
    reason = Column(String(200))