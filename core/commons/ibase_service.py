from abc import abstractmethod
from typing import TypeVar
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs.dev_config import DATABASE
T= TypeVar("T")

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost/dun"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SQLALCHEMY_DATABASE_URL = "postgresql://%s:%s@%s/%s"


        
class IBaseService:
    def __init__(self):
        self.db = SessionLocal()
        try:
            self.db
        finally:
            self.db.close()
            
    
        
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
        
    
# class PgService:
#     def __init__(self):
       
#         self.DB_URL = SQLALCHEMY_DATABASE_URL % (DATABASE['default']['user'], DATABASE['default']['password'],
#                                             DATABASE['default']['host'], DATABASE['default']['db_name'])
#         self.engine = create_engine(self.DB_URL)
#         self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
#     def __call__(self):
#             pass
                       

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


