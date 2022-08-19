from pydantic import BaseModel, Field
from uuid import UUID


class WorkUnitAddRequest(BaseModel):
    name : str  = None

class WorkUnitUpdateRequest(WorkUnitAddRequest):
    id: UUID = None

class WorkUnitAddListRequest(BaseModel):
    work_unit_items : list [WorkUnitAddRequest] = Field(..., min_items=1,unique_items=True)

class WorkUnitUpdateListRequest(BaseModel):
    work_unit_items : list [WorkUnitUpdateRequest] = Field(None,unique_items=True)
    
class WorkUnitTeacher(BaseModel):
    name : str =None
    level : str =None
    specialize : str =None
    work_unit_id : UUID = None
    class Config:
            orm_mode = True

class WorkUnitResponse(WorkUnitAddRequest):
    id: UUID = None
    teachers: list[WorkUnitTeacher] = []
    
    class config:
        orm_mode = True