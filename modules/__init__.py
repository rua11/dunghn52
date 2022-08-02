import os
import importlib
#from modules.users import router
routes = []
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] == '.py' or module == '__pycache__' or module == '.DS_Store':
        continue
    routes.append(__import__(module+'.router', locals(), globals(), level=1))
del module
 
def router_builder(app):
    try:
        for route in routes:
            app.include_router(router=route.routes, prefix='/api/v1%s' % route.prefix_url)


    except:
        raise Exception("error!")