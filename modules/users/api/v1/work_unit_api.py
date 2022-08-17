from uuid import UUID
from fastapi import APIRouter, Depends
from core.commons.base_schema import BaseSchemaSearchRequest
from core.commons.context import ErrorsReponse, ExceptionResponse, SuccessResponse
from modules.users.schemas.work_unit_schema import WorkUnitAddListRequest, WorkUnitAddRequest, WorkUnitUpdateListRequest, WorkUnitUpdateRequest
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
        return ExceptionResponse(errors=str(ex.args))

@router.post('/add-work-unit' )
def add_work_unit(request: WorkUnitAddRequest):
    try:
        res = WorkUnitService().add_work_unit(request= request)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))


@router.post('/add-list-work-unit')
def add_list_work_unit(request: WorkUnitAddListRequest):
    try:
        res = WorkUnitService().add_list(request= request)
        if res:
            return SuccessResponse(message="ass thanh cong")
        return ErrorsReponse(message= "da xay ra loi, hay thu lai")
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))

@router.get('/get-work-unit/{id}')
def get_work_unit(id: UUID):
    try:
        res = WorkUnitService().filter_object_by_id(value=id)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))


@router.post('/update-work-unit')
def update_work_unit(request: WorkUnitUpdateRequest):
    try:
        res = WorkUnitService().update_work_unit(request=request)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))

    
@router.post('/update-list-work-unit')
def update_list_work_unit(request: WorkUnitUpdateListRequest):
    try:
        res = WorkUnitService().update_list(request=request)
        if res:
            return SuccessResponse(message="da update thanh cong")
        return ErrorsReponse(message="da xay ra loi, hay thu lai")
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))

    