from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()
class BaseModel(Base):
    __abstract__ = True
    id= Column(UUID(as_uuid=True), index=True, primary_key= True,default=uuid.uuid4)
