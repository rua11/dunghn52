from abc import abstractmethod
from core.commons.ibase_service import IBaseService
from modules.users.schemas.teacher_schema import TeacherAddRequest, TeacherResponse, TeacherUpdateRequest
from modules.users.models.teacher_model import Teacher
class ITeacherService(IBaseService):
    

    @abstractmethod
    def search(self, request):
        T = Teacher
        numeric_fields = []
        schema_response = TeacherResponse
        return super().search(T=T, request = request, numeric_fields = numeric_fields, schema_response= schema_response)
    @abstractmethod
    def add_teacher(self, request: TeacherAddRequest):
        return super().add(T = Teacher, value = request)
    
    @abstractmethod
    def update_teacher(self, request: TeacherUpdateRequest):
        return super().update(T = Teacher, value = request)
    
    @abstractmethod
    def filter_teacher_by_id(self, id):
        return super().filter_object_by_id(T= Teacher, key = Teacher.id, value = id)
    
    @abstractmethod
    def delete_teacher(self, key, value):
        return super().delete(T= Teacher, key = Teacher.id, value = value)
    
    
class TeacherService(ITeacherService):
    pass