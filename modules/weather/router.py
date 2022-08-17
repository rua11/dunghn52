from fastapi import APIRouter
from modules.weather.api.v1 import weather_api

prefix_url = '/weather' 


routes = APIRouter() 
routes.include_router(weather_api.router)