from fastapi import APIRouter

from modules.users.schemas.work_unit_schema import WorkUnitAddRequest
from modules.users.service.work_unit_service import WorkUnitService


router = APIRouter(
    prefix="/work_unit",
    tags=["Quản Lý Đơn Vị Công Tác"],
    responses={404: {"description": "Not found"}},
)
@router.post('/path_name')
async def method_name():
    pass
# @router.post('/add-work-unit')
# async def add_work_unit():
#     try:
#         res = WorkUnitService.add()
        
    