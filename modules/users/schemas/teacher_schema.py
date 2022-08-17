from uuid import UUID
from pydantic import BaseModel

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
    id : UUID = None
    name : str  = None

class TeacherSubjectClassResponse(BaseModel):
    name : str 
    teacher_id : UUID = None
    
class TeacherRollCallResponse(BaseModel):
    teacher_id : UUID
    subject_classes_id : UUID 
    semester :str = None
    year :str = None
    
    
class TeacherResponse(TeacherUpdateRequest):
    work_unit : TeacherWorkUnitResponse = []
    subject_classes : list[TeacherSubjectClassResponse]= []
    roll_calls : list [TeacherRollCallResponse] = []