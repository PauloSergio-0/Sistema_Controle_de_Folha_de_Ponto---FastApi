from fastapi import APIRouter

    
router = APIRouter()

@router.get('/test')
def teste():
    return {'message': 'tes'}