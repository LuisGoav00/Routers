#en vez de importar el framework, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter

router = APIRouter()
#en vez de fastapi: con APIRouter
@router.get("/producto/")

#???Instancia del producto
async def userclass():
        return("Producto1","Producto2","Producto3","Producto4","Producto5") 