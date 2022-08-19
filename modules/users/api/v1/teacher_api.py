from datetime import date
from uuid import UUID
from fastapi import APIRouter, Depends

from core.commons.base_schema import BaseSchemaSearchRequest
from modules.users.schemas.teacher_schema import TeacherAddRequest, TeacherUpdateRequest

from core.commons.context import ErrorsReponse, ExceptionResponse, SuccessResponse

from ...service.teacher_service import TeacherService

router = APIRouter(
    prefix = '/teacher', 
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
      


@router.post('/add-teacher')
def add_teacher(request: TeacherAddRequest):
    try:
        res = TeacherService().add_teacher(request=request)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))

@router.post('update-teacher')
def update_teacher(request: TeacherUpdateRequest):
    try:
        res = TeacherService().update_teacher(request= request)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ExceptionResponse(errors= str(ex.args))
    
@router.get('/get-teacher-by-id/{id}')
def get_teacher_by_id(id: UUID):
    try:
        res = TeacherService().filter_teacher_by_id(id= id)
        if res:
            return SuccessResponse(data= res)
        return ErrorsReponse(message="teacher khong ton tai")
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))
    
@router.delete('/delete-teacher')
def  delete_teacher(id: UUID):
    try:
        res = TeacherService().delete_teacher(value= id)
        if res is None:
            return {"Xoas Thanh Cong"}
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))
            
    
