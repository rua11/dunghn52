from abc import abstractmethod
from core.commons.ibase_service import IBaseService
from core.commons.ibase_service_mongo import IBaseMongo
# from ....core.commons.ibase_service_mongo import IBaseMongo
from modules.weather.models.weather_model import WeatherModel
import requests
import json
import time
from bson import Binary

class IWeatherService(IBaseService):
    lang = 'vi'
    key = '55a68c065171b9421a937ff88c3e3e6f'
    
    @abstractmethod
    def add_weather(self, request):
        return super().add(T = WeatherModel , value = request)
    @abstractmethod
    def query_all_weather(self):
        return super().query_all(T=WeatherModel)
class WeatherService(IWeatherService):
    pass

class WeatherServiceBase():
    async def job():
        res = WeatherService().query_all_weather().all()
        i = 0
        print(len(res))
        for item in res:
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={item.lat}&lon={item.lon}&lang={WeatherService.lang}&appid={WeatherService.key}'
            response1 = requests.get(url = url) 
            ress = json.loads(response1.text)
            print(ress)
            
            itemmg = {}
            itemmg['user_id'] = Binary.from_uuid(item.id)
            itemmg['lat'] = item.lat
            itemmg['lon'] = item.lon
            itemmg['address'] = item.address
            itemmg['name'] = item.name
            
            response2 = await IBaseMongo().get_one_field(value = itemmg)
            # print(response2)
            
            if response2 is None:
                itemmg['data'] = ress
                
                await IBaseMongo().add(itemmg)
            else:
                itemmg = {}
                itemmg['data'] = ress
                await IBaseMongo().update_one(id= response2['_id'] , value= itemmg)
                
            i += 1
            if i == 2:
                print('dang nghi')
                time.sleep(15)
                i = 0
            