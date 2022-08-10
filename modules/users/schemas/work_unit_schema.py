from pydantic import BaseModel
from uuid import UUID


class WorkUnitAddRequest(BaseModel):
    name : str  = None

class WorkUnitUpdateRequest(WorkUnitAddRequest):
    id: UUID
    
class WorkUnitTeacher(BaseModel):
    name : str =None
    level : str =None
    specialize : str =None
    work_unit_id : UUID = None
    class Config:
            orm_mode = True
    
class WorkUnitResponse(WorkUnitAddRequest):
    # work_unit: WorkUnitTeacher = []
    pass
    class config:
        orm_mode = True