from fastapi import APIRouter


router = APIRouter(
    prefix="/work_unit",
    tags=["Quản Lý Đơn Vị Công Tác"],
    responses={404: {"description": "Not found"}},
)

@router.post('/path_name')
async def method_name():
    pass