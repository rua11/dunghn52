from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String,  Float
from core.commons.base_model import BaseModel as Base

class WeatherModel(Base):
    __tablename__ = 'waether'
    lat = Column(Float)
    lon = Column(Float)
    address = Column(String)
    name = Column(String)
    