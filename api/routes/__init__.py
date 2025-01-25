from .funcionario_routes import router as funcionario
from fastapi import FastAPI

def init_router(app: FastAPI):
    app.include_router(funcionario)