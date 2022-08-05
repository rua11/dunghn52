from abc import abstractmethod
from bson import json_util
import json

from typing import TypeVar
from bson import ObjectId
import motor.motor_asyncio
myclient = "mongodb://localhost:27017/"
client = motor.motor_asyncio.AsyncIOMotorClient(myclient)
db = client.school
col = db.eeeeee

class IBaseMongo:
    def __init__(self):
        self.db = db
        self.col = col
        
    @abstractmethod
    def add(self, value):
        try:
            object = self.col.insert_one(value)
            return object
        except Exception as ex:
            raise ex
        
    @abstractmethod
    def get_one(self, value):
        try:
            object = self.col.find_one({"_id": value})
            return object
        except Exception as ex:
            raise ex
    
    @abstractmethod
    def get_list(self, value):
        try:
            object = self.col.find().to_list(value)
            return object
        except Exception as ex:
            raise ex
        
    
