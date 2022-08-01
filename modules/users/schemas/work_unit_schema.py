from pydantic import BaseModel


class WorkUnitAddRequest(BaseModel):
    name : str = None
    
class WorkUnitResponse(WorkUnitAddRequest):
    pass 
    class config:
        orm_mode = True