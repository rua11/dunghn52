from fastapi import FastAPI
# from core.commons import base_model 
# from core.commons.ibase_service import engine
from modules import router_builder

# base_model.Base.metadata.create_all(bind=engine)
app = FastAPI()

router_builder(app)

@app.get('/hello')
async def method_name():
    return {"message": "Hello World"}