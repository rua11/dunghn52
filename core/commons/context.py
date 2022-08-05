from typing import TypeVar, Generic
from pydantic.generics import GenericModel
from datetime import datetime
from fastapi import status
T= TypeVar('T')


class BaseResponse(GenericModel, Generic[T]):
    version: str = 'Project for You'
    response_time: str = (datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    message: str = None
    errors: T = None
    data : T = None
    
class SuccessResponse(BaseResponse):
    code : int = status.HTTP_200_OK
    status : bool = True
    
class ErrorsReponse(BaseResponse):
    code: int= status.HTTP_404_NOT_FOUND
    status : bool = False
    
class ExceptionResponse(BaseResponse):
    code: int = status.HTTP_400_BAD_REQUEST
    status: bool = False
    message: str = "Có lỗi xảy ra."

    