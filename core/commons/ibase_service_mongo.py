from abc import abstractmethod
from uuid import UUID
from bson import json_util, Binary


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
    def get_one_field(self, value):
        try:
            object = self.col.find_one(value)
            return object
        except Exception as ex:
            raise ex

    @abstractmethod
    def get_one(self, value):
        try:
            object = self.col.find_one({"_id": ObjectId(value)})
            return object
        except Exception as ex:
            raise ex
    
    @abstractmethod
    def get_one_user(self,value):
        try:
            object = self.col.find_one({"user_id": Binary.from_uuid(value)})
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
    
    @abstractmethod
    def search(self,value):
        try:
            object = self.col.find({"name":  { "$regex": "[{}]".format(value) }}).to_list(100000)
            return object
        except Exception as ex:
            raise ex
        
    @abstractmethod
    def update_one(self, value, id):
        try:
            object = self.col.update_one({"_id":ObjectId(id)}, {"$set": value})
            return object               
        except Exception as ex:
            raise ex
        
    @abstractmethod
    def delete_one(self, value):
        try:
            object = self.col.delete_one({'_id': value})
            return object
        except Exception as ex:
            raise ex
        
    
