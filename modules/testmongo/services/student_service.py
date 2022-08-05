from abc import abstractmethod
from core.commons.ibase_service_mongo import IBaseMongo
from modules.testmongo.schemas.student_schema import StudentRequest

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
    
class StudentMongo(IStudentMongo):
    pass