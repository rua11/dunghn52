import uuid
from fastapi import APIRouter, Depends

from core.commons.base_schema import BaseSchemaSearchRequest

from .....core.commons.context import ErrorsReponse, ExceptionResponse, SuccessResponse

from ...service.teacher_service import TeacherService

router = APIRouter(
    tags=["Quản Lý Giáo Viên"],
    responses={404: {"description": "Not found"}},
)


@router.get('/search')
def search(request: BaseSchemaSearchRequest = Depends()):
    try:
        res = TeacherService().search(request= request)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))    
@router.get('/get-teacher-by-id/{id}')
def get_teacher_by_id(id: uuid):
    try:
        res = TeacherService().filter_teacher_by_id(id= id)
        if res:
            return SuccessResponse(data= res)
        return ErrorsReponse(message="teacher khong ton tai")
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))
    
