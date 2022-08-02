from fastapi import APIRouter
from modules.users.schemas.work_unit_schema import WorkUnitAddRequest, WorkUnitResponse
from modules.users.service.work_unit_service import WorkUnitService


router = APIRouter(
    tags=["Quản Lý Đơn Vị Công Tác"],
    responses={404: {"description": "Not found"}},
)

@router.post('/add-work-unit')
async def add_work_unit(request: WorkUnitAddRequest):
    try:
        res = WorkUnitService().add_work_unit(request= request)
        return res
    except Exception as ex:
        return ex

    
        
    