#en vez de importar el framework, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel #Importamos pydantic para obtener una entidad que pueda definir usuarios


router = APIRouter()
#en vez de fastapi: con APIRouter

#Definimos nuestra entidad User (utilizando BaseModel):
class User (BaseModel):
    Tid:int
    Marca:str
    Modelo:str

users_list=  [
User(Tid=1,Marca="Nike",Modelo="Air 10"),
User(Tid=2,Marca="Adidas",Modelo="Falcon running"),
User(Tid=3,Marca="Nike",Modelo="Curry")   
]

@router.get("/tenis/", status_code=status.HTTP_200_OK)
async def tenis():
    return users_list

#Función Get con Filtro Path
@router.get("/tenis/{id}",status_code=status.HTTP_200_OK)
async def usersclass(id: int):#Esta variable tiene que ser la misma que en la línea 57
    users = filter(lambda user: user.Carroid == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
