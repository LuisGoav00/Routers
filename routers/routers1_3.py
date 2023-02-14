#en vez de importar el framework, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter

router = APIRouter()
#en vez de fastapi: con APIRouter
@router.get("/telefonos/")

#???Instancia del producto
async def userclass():
        return("Samsumg","Iphone","Xiaomi","Oppo","Lg") 