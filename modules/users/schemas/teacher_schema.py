import json
from uuid import UUID
from pydantic import BaseModel, validator

class TeacherBase(BaseModel):
    name :str
    level :str = None
    specialize: str = None
    work_unit_id : UUID
    
class TeacherAddRequest(TeacherBase):
    pass

class TeacherUpdateRequest(BaseModel):
    id : UUID = None
    name :str = None
    level :str = None
    specialize: str = None
    work_unit_id : UUID = None

class TeacherWorkUnitResponse(BaseModel):
    # id : UUID = None
    name : str  = None
    class Config:
            orm_mode = True

class TeacherSubjectClassResponse(BaseModel):
    name : str 
    teacher_id : UUID = None
    class Config:
            orm_mode = True
    
class TeacherRollCallResponse(BaseModel):
    teacher_id : UUID
    subject_classes_id : UUID 
    semester :str = None
    year :str = None
    class Config:
            orm_mode = True
    
    
class TeacherResponse(TeacherAddRequest):
    id: UUID = None
    work_unit : TeacherWorkUnitResponse = []
    subject_classes : list[TeacherSubjectClassResponse]= []
    roll_calls : list[TeacherRollCallResponse] = []
    class config:
        orm_mode = True


class TeacherWorkUnitResponse1(BaseModel):
    id: UUID = None
    name: str  = None
    @validator('id')
    def validate(cls, v):
        v.id= str(v.id)
        return v
            
class TeacherGrpcResponse(BaseModel):
    id: UUID
    name :str
    level :str = None
    specialize: str = None
    work_unit_id : UUID
    work_unit:TeacherWorkUnitResponse1
    @validator('work_unit_id','id')
    def validate(cls, v):
        if not isinstance(v, UUID):
            raise TypeError('ObjectId required2')
        return str(v)
    class Config:
        orm_mode = True
        
    
    
        