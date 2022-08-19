import asyncio
from datetime import date
from fastapi import APIRouter, status
import time
from core.commons.context import ExceptionResponse, SuccessResponse
from core.commons.ibase_service_mongo import IBaseMongo

from ...service.weather_service import  WeatherService, WeatherServiceBase

from ...schemas.weather_schema import WeatherRequest, WeatherResponse
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json
import requests
from fastapi.responses import JSONResponse
from bson import json_util, ObjectId
from uuid import UUID





router = APIRouter(
    tags=["Test Weather"],
    responses={404: {"description": "Not found"}},
)

@router.post('/test-add-weather' )
def test_add_weather(request: WeatherRequest):
    try:
        res = WeatherService().add_weather(request= request)
        return SuccessResponse(data= res)
    except Exception as ex:
        return ExceptionResponse(errors=str(ex.args))
    

# async def job():
#     res = WeatherService().query_all_weather().all()
#     i = 0
#     print(len(res))
#     for item in res:
#         url = f'https://api.openweathermap.org/data/2.5/weather?lat={item.lat}&lon={item.lon}&lang={WeatherService.lang}&appid={WeatherService.key}'
#         response = requests.get(url = url) 
#         res = response.text
#         print(res)
#         await (IBaseMongo().add(json.loads(res)))
#         i += 1
#         if i == 2:
#             print('dang nghi')
#             time.sleep(60)
#             i = 0
        
        
# apschedule api
# @router.on_event("startup")
# def init_data():
#     trigger = CronTrigger(hour = 15, minute = 57, second=40)
#     scheduler = AsyncIOScheduler()
#     scheduler.add_job(WeatherServiceBase.job, trigger=trigger)
#     # scheduler.add_job(WeatherServiceBase.job, "interval", seconds = 5)
    
#     scheduler.start()
    
@router.get('/get-object-weather')
async def get_object_weather(id: str):
    try:
        res = await IBaseMongo().get_one(value=id)
        # a = json_util.dumps(res)
        # b = json.loads(a)
        
        # return JSONResponse(status_code=status.HTTP_201_CREATED, content=b)
        # print(res['_id'])
        res['id'] = str(res['_id'])
        return SuccessResponse(data= WeatherResponse(**res))
    except Exception as ex:
        raise ex
    
@router.get('/get-object-weather-by-user-id')
async def get_object_weather_by_user_id( id: UUID):
    try:
        res = await IBaseMongo().get_one_user(value=id)
        # a = json_util.dumps(res)
        # b = json.loads(a)
        
        # return JSONResponse(status_code=status.HTTP_201_CREATED, content=b)
        # print(res['_id'])
        res['id'] = str(res['_id'])
        return SuccessResponse(data= WeatherResponse(**res))
    except Exception as ex:
        raise ex