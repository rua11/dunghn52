from abc import abstractmethod
from core.commons.ibase_service import IBaseService
from modules.users.schemas.teacher_schema import TeacherAddRequest, TeacherResponse, TeacherUpdateRequest
from modules.users.models.teacher_model import Teacher
class ITeacherService(IBaseService):
    
    @abstractmethod
    def search(self, T, request, numeric_fields: list[str], schema_response, additional_func=None):
        T = Teacher
        numeric_fields = []
        schema_response = TeacherResponse
        return super().search(schema_response = schema_response)
    @abstractmethod
    def add_teacher(self, request: TeacherAddRequest):
        return super().add(T = Teacher, value = request)
    
    @abstractmethod
    def update_teacher(self, request: TeacherUpdateRequest):
        return super().update(T = Teacher, value = request)
    
    @abstractmethod
    def filter_teacher_by_id(self, id):
        return super().filter_object_by_id(T= Teacher, key = Teacher.id, value = id)
    
    
class TeacherService(ITeacherService):
    pass