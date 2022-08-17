from uuid import UUID
from bson import ObjectId
from pydantic  import Field

from bson import ObjectId
from pydantic import BaseModel, Field
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string") 
        

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

    user_id : UUID
    lat : float
    lon : float
    address : str
    name : str
    data : dict
    class Config:
        orm_more = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}