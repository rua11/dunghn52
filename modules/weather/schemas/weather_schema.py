from uuid import UUID
from bson import ObjectId
from pydantic  import Field

from bson import ObjectId
from pydantic import BaseModel, Field

from pydantic import BaseModel
class WeatherBase(BaseModel):
    lat : float
    lon : float
    address : str
    name : str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "lat": "21.026551",
                "lon": "105.849338",
                "address": "Tràng Thi - Hà Nội",
                "name": "Ông Dũng Địa Chủ",
            }
        }
    
class WeatherRequest(WeatherBase):
    pass 

class WeatherResponse(WeatherBase):
    id : str = None
    user_id : UUID=None
    lat : float=None
    lon : float=None
    address : str=None
    name : str=None
    data : dict=None
    class Config:
        orm_more = True
        