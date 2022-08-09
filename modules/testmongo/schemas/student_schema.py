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
        
class StudentRequest(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    course: str = Field(...)
    gpa: float = Field(..., le=4.0)

    class Config:
            allow_population_by_field_name = True
            arbitrary_types_allowed = True
            json_encoders = {ObjectId: str}
            schema_extra = {
                "example": {
                    "name": "Anh Dung Dep Trai",
                    "email": "ngocdungnb06@gmail.com",
                    "course": "Experiments, Science, and Fashion in Nanophotonics",
                    "gpa": "4.0",
                }
            }
            
            
class StudentUpdateRequset(BaseModel):
    name: str =None
    email: str =None
    course: str =None
    gpa: float =None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
                "example": {
                    "name": "Anh Dung Dep Trai",
                    "email": "ngocdungnb06@gmail.com",
                    "course": "Experiments, Science, and Fashion in Nanophotonics",
                    "gpa": "4.0",
                }
            }
class StudentResponse(BaseModel):
    name: str =None
    email: str =None
    course: str =None
    gpa: float =None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
       
class StudentListResponse(BaseModel):
    student_list : list[StudentResponse] = None
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}