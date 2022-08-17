from typing import List
from fastapi import APIRouter
from core.commons.context import ExceptionResponse, SuccessResponse
import json
from bson import json_util
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder



from modules.testmongo.schemas.student_schema import StudentListResponse, StudentRequest, StudentResponse, StudentUpdateRequset
from modules.testmongo.services.student_service import StudentMongo


router = APIRouter(
    tags=["Quản lý sinh viên"],
    responses={404: {"description": "Not found"}},)

@router.post('/add-student')
async def add_student(request: StudentRequest):
    try:
        request = jsonable_encoder(request)        
        res = await StudentMongo().add_student(request=request)
        if res != None:
            return SuccessResponse(data= StudentResponse(**request))
        # new_student= (StudentRequest(**request))
        # print(new_student)
        # new_student.id=str(res.inserted_id)
        # new_student = json.loads(json_util.dumps(a))
        # get_student = StudentMongo().get_student(id= res.inserted_id)
        # print(get_student)
        # return JSONResponse(content=new)
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))

@router.get('/get-student-by-id')
async def get_student_by_id(id:str):
    try:
        res = await StudentMongo().get_student(id=id)
        
        return SuccessResponse(data=StudentResponse(**res))
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))
    
@router.get('/get-list-student')
async def get_list_student(number: int):
    try:
        res = await StudentMongo().get_list_student(value=number)
        return SuccessResponse(data=StudentListResponse(student_list=res))
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))
    
@router.post('/search-student-by-name')
async def search_student_by_name(name: str):
    try:
        res = await StudentMongo().search(value= name)
        return SuccessResponse(data=StudentListResponse(student_list= res))
    except Exception as ex:
        return ExceptionResponse(errors= str(ex.args))
    
@router.post('/update-student')
async def update_student(id: str, request: StudentUpdateRequset):
    try:
        oj = await StudentMongo().get_student(id=id)
        if oj:
            await StudentMongo().update_sutdent(request= request, id= id)      
         
        return SuccessResponse(data=StudentResponse(**oj))
    except Exception as ex:
        return SuccessResponse(errors=str(ex.args))
    
@router.delete('/delete-student')
async def delete_student(id : str):
    try:
        
        await StudentMongo().delete_student(id= id)
        return {'Success':'Xoas Thanhf Coong'}
    except Exception as ex:
        return SuccessResponse(errors=str(ex.args))  
        
        