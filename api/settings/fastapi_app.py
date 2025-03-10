from fastapi import FastAPI
from routes import init_router

def app():
    app = FastAPI()
    init_router(app)
    
    
    return app
