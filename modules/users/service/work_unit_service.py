from abc import abstractmethod
from core.commons.ibase_service import IBaseService
from modules.users.models.work_unit_model import WorkUnit
from modules.users.schemas.work_unit_schema import WorkUnitAddRequest, WorkUnitUpdateRequest


class IWorkUnitService(IBaseService):
    
    @abstractmethod
    def add_work_unit(self,request : WorkUnitAddRequest):
        return super().add(T = WorkUnit, value = request)
    
    @abstractmethod
    def update_work_unit(self, request: WorkUnitUpdateRequest):
        return super().update(T = WorkUnit, value = request)
    
    @abstractmethod
    def filter_object_by_id(self, value):
        return super().filter_object_by_id(T = WorkUnit, key = WorkUnit.id, value = value)
    
class WorkUnitService(IWorkUnitService):
    pass