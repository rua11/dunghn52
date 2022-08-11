from uuid import UUID
from fastapi import APIRouter, Depends
from core.commons.base_schema import BaseSchemaSearchRequest
from core.commons.context import SuccessResponse
from modules.users.schemas.work_unit_schema import WorkUnitAddRequest, WorkUnitResponse, WorkUnitUpdateRequest
from modules.users.service.work_unit_service import WorkUnitService

router = APIRouter(
    tags=["Quản Lý Đơn Vị Công Tác"],
    responses={404: {"description": "Not found"}},
)

@router.get('/search')
def search(request: BaseSchemaSearchRequest = Depends()):
    try:
        res = WorkUnitService().search(request= request)
        if res:
            return SuccessResponse(data = res)
    except Exception as ex:
        return ex

@router.post('/add-work-unit' )
def add_work_unit(request: WorkUnitAddRequest):
    try:
        res = WorkUnitService().add_work_unit(request= request)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ex

@router.get('/get-work-unit/{id}')
def get_work_unit(id: UUID):
    try:
        res = WorkUnitService().filter_object_by_id(value=id)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ex

@router.post('/update-work-unit')
def update_work_unit(request: WorkUnitUpdateRequest):
    try:
        res = WorkUnitService().update_work_unit(request=request)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ex
    