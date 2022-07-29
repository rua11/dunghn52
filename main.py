from fastapi import FastAPI
from core.commons import base_model 
#aa


from core.commons.ibase_service import engine
base_model.Base.metadata.create_all(bind=engine)
app = FastAPI()