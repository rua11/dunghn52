
from fastapi import APIRouter

from modules.users.api.v1 import teacher_api, work_unit_api


prefix_url = '/diemdanh' 


routes = APIRouter() 
routes.include_router(work_unit_api.router)
routes.include_router(teacher_api.router)