from fastapi import APIRouter, UploadFile, status, HTTPException
from service.service_funcionario import Service_funcionario
    
router = APIRouter()

@router.post('/funcionario/importar')
async def importar_dado(file: UploadFile = (...)):
    await Service_funcionario.importar_funcionario(file)
    return {'message': 'tes'}