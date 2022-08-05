from fastapi import APIRouter
from modules.testmongo.api.v1 import student_api

prefix_url = '/testmongo' 


routes = APIRouter() 
routes.include_router(student_api.router)
