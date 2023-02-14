#en vez de importar el framework, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel #Importamos pydantic para obtener una entidad que pueda definir usuarios


router = APIRouter()
#en vez de fastapi: con APIRouter

#Definimos nuestra entidad User (utilizando BaseModel):
class User (BaseModel):
    Carroid:int
    Marca:str
    Placas:str

users_list=  [
User(Carroid=1,Marca="Chevrolet",Placas="AD4-7DE"),
User(Carroid=2,Marca="Nissan",Placas="X77-4DE"),
User(Carroid=3,Marca="Ford",Placas="D33-444")   
]

@router.get("/carros/", status_code=status.HTTP_200_OK)
async def carros():
    return users_list

#Función Get con Filtro Path
@router.get("/carros/{id}",status_code=status.HTTP_200_OK)
async def usersclass(id: int):#Esta variable tiene que ser la misma que en la línea 57
    users = filter(lambda user: user.Carroid == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
