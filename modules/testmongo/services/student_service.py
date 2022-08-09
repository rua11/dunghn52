from abc import abstractmethod
from core.commons.ibase_service_mongo import IBaseMongo
from modules.testmongo.schemas.student_schema import StudentRequest, StudentUpdateRequset

class IStudentMongo(IBaseMongo):
    @abstractmethod
    def add_student(self, request: StudentRequest):
        return super().add(value = request)
    
    @abstractmethod
    def get_student(self, id):
        return super().get_one(value = id)
    
    @abstractmethod
    def get_list_student(self, value):
        return super().get_list(value = value)
    
    @abstractmethod
    def update_sutdent(self, request: StudentUpdateRequset, id):
        return super().update_one(value= request, id= id)
    
    def delete_student(self, id):
        return super().delete_one(value = id)
    
class StudentMongo(IStudentMongo):
    pass
