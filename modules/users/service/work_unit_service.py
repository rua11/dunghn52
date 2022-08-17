from abc import abstractmethod
from urllib import request
from core.commons.ibase_service import IBaseService
from modules.users.models.work_unit_model import WorkUnit
from modules.users.schemas.work_unit_schema import WorkUnitAddListRequest, WorkUnitAddRequest, WorkUnitResponse, WorkUnitUpdateListRequest, WorkUnitUpdateRequest


class IWorkUnitService(IBaseService):
    
    @abstractmethod
    def search(self, request):
        T =WorkUnit
        numeric_fields = []
        schema_response = WorkUnitResponse
        return super().search(T=T, request = request, numeric_fields = numeric_fields, schema_response= schema_response)
    
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
    def add_list(self, request: WorkUnitAddListRequest):
        try:
            for item in request.work_unit_items:
                self.add(T = WorkUnit, value = item)
            return True
        except Exception as ex:
            raise ex
        
    def update_list(self, request: WorkUnitUpdateListRequest ):
        try:
            if request.work_unit_items != None:
                for item in request.work_unit_items:
                    if item.id:
                        # item = WorkUnitUpdateRequest(**item.dict())
                        IWorkUnitService().update_work_unit(request= item)
                    else:
                        # item = WorkUnitAddRequest(**item.dict())
                        IWorkUnitService().add_work_unit(request=item)
                return True
        except Exception as ex:
            self.db.rollback()
            raise ex
