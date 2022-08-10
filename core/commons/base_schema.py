from typing import TypeVar
from  uuid import UUID
from pydantic import BaseModel, Field

T = TypeVar('T')


class PageResponse(BaseModel):
    pagenum: int
    pagesize: int
    total_page: int
    total: int
    items: T = None
    class Config:
        orm_mode = True
        
class PageRequest(BaseModel):
    pagenum: int = Field(default=1)
    pagesize: int = Field(default=1, gt= 0)
    
class BaseSchemaRequest(BaseModel):
    id: UUID = None
    
class BaseSchemaAddRequest(BaseSchemaRequest):
    pass

class BaseSchemaUpdateRequest(BaseSchemaRequest):
    id: UUID
    
class SchemaRequest(BaseSchemaAddRequest, BaseSchemaUpdateRequest):
    pass 

class BaseSchemaUpdateStatusRequest(BaseSchemaUpdateRequest):
    id: UUID
    
class BaseSchemaResponse(BaseSchemaAddRequest,BaseSchemaUpdateRequest):
    pass 
    class Config:
        orm_mode=True
    
class BaseSchemaSearchRequest(PageRequest):
    query:str=None
    queryfields:str=None
class BaseSchemaListResponse(PageResponse):
    class Config:
        orm_mode = True