from fastapi import FastAPI
from core.commons import base_model 
from core.commons.ibase_service import engine
from modules.users.api.v1 import work_unit_api

base_model.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(work_unit_api.router)
