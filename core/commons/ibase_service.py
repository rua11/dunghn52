from abc import abstractmethod
import math
from typing import TypeVar
from sqlalchemy import create_engine, or_, desc
from sqlalchemy.orm import sessionmaker
from configs.dev_config import DATABASE
from .base_schema import BaseSchemaListResponse
T= TypeVar("T")

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost/dun"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SQLALCHEMY_DATABASE_URL = "postgresql://%s:%s@%s/%s"


     
class IBaseService:
    def __init__(self):
        self.db = PgService().SessionLocal()
        try:
            self.db
        finally:
            self.db.close()
        super().__init__()
    
    @abstractmethod    
    def search(self, T, request,numeric_fields:list[str], schema_response, additional_func=None):
        
        try:
            _page_index = request.pagenum if  request.pagenum >0 else 1
            _page_size = request.pagesize
            query = self.query_all(T=T)
            numeric_fields+=[]
            if additional_func!=None:
                query=additional_func()
                
            if request.queryfields:
                queryfields = request.queryfields.split(",")
                query = query.filter(or_(getattr(T, field).ilike(f'%{request.query}%') if field not in numeric_fields else getattr(
                    T, field) == float(request.query) for field in queryfields))
            _total = query.count()
            _total_page = math.ceil(_total/_page_size)
            query = query.order_by(desc(T.id)).limit(
                _page_size).offset((_page_index-1)*_page_size).all()
            _list = [schema_response(**item.__dict__) for item in query]
            response = BaseSchemaListResponse(
                pagenum=_page_index,
                pagesize=_page_size,
                total_page=_total_page,
                total=_total,
                items=_list
            )
            return response
        except Exception as ex:
            raise(ex)    
        
        
    @abstractmethod
    def query_all(self, T):
        try:
            object = self.db.query(T)
            return object
        except Exception as ex:
            raise ex
     
    @abstractmethod
    def add(self, T, value):
        try:
            object=T(**value.dict())
            self.db.add(object)
            self.db.commit()
            self.db.refresh(object)
            return object
        except Exception as ex:
            self.db.rollback()
            raise(ex)
    
    @abstractmethod
    def filter_object_by_id(self,T,key,value):
        try: 
            object = self.db.query(T).filter(key == value)
            return object.first()
        except Exception as ex:
            raise ex
    
    @abstractmethod
    def filter_object(self, T,key, value):
        object=self.db.query(T).filter(key==value)
        return object
        
    @abstractmethod
    def update(self, T, value):
        try:
            
            object= self.db.query(T).filter(T.id==value.id)
            if object.first():
                value = dict(filter(lambda item: item[1] is not None, value.dict().items()))
                object.update(value)
                self.db.commit()
                return object.first()
            return None
        except Exception as ex:
            self.db.rollback()
            raise(ex)
        
    @abstractmethod
    def delete(self,T, key, value):
        try:
            obj = self.filter_object(T,key,value)
            for item in obj:
                self.db.delete(item)
            self.db.commit()
        except Exception as ex:
            self.db.rollback()
            raise ex
    
    @abstractmethod
    def delete_all(self, T):
        try:
            self.db.query(T).delete()
        except Exception as ex:
            self.db.rollback()
            raise ex
    

    
        
        
    
class PgService:
    def __init__(self):
       
        self.DB_URL = SQLALCHEMY_DATABASE_URL % (DATABASE['default']['user'], DATABASE['default']['password'],
                                            DATABASE['default']['host'], DATABASE['default']['db_name'])
        self.engine = create_engine(self.DB_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    def __call__(self):
            pass
                       
