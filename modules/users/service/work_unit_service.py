from abc import abstractmethod
from core.commons.ibase_service import IBaseService
from modules.users.models.work_unit_model import WorkUnit
from modules.users.schemas.work_unit_schema import WorkUnitAddRequest


class IWorkUnitService(IBaseService):
    
    @abstractmethod
    def add_work_unit(self,request : WorkUnitAddRequest):
        return super().add(T = WorkUnit, value = request)
    
    
class WorkUnitService(IWorkUnitService):
    pass