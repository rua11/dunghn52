from abc import abstractmethod
from typing import TypeVar
from bson import ObjectId
import motor.motor_asyncio
myclient = "mongodb://localhost:27017/"

client = motor.motor_asyncio.AsyncIOMotorClient(myclient)

db = client.school
col = db.student

class IbaseMongo:
    def __init__(self, col):
        self.db = db
        self.col = col
        self.mycol = self.db['self.coll']
        
    @abstractmethod
    async def add(self, value):
        try:
            object = await self.mycol.insert_one[value.dict()]
            return object
        except Exception as ex:
            raise ex
        
    @abstractmethod
    async def get_one(self, value):
        try:
            object = await self.mycol.find_one({"_id": ObjectId(value.inserted_id)})
            return object
        except Exception as ex:
            raise ex
    
    @abstractmethod
    async def get_list(self, value):
        try:
            object = await self.mycol.find().list(value)
            return object
        except Exception as ex:
            raise ex
        
    
