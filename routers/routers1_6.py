#en vez de importar el framework, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel #Importamos pydantic para obtener una entidad que pueda definir usuarios


router = APIRouter()
#en vez de fastapi: con APIRouter

#Definimos nuestra entidad User (utilizando BaseModel):
class User (BaseModel):
    Celid:int
    Marca:str
    Año:str

users_list=  [
User(Celid=1,Marca="Samsumg",Año="2013"),
User(Celid=2,Marca="Huawei",Año="2017"),
User(Celid=3,Marca="Iphone",Año="2020")   
]

@router.get("/celulares/", status_code=status.HTTP_200_OK)
async def celulares():
    return users_list

#Función Get con Filtro Path
@router.get("/celulares/{id}",status_code=status.HTTP_200_OK)
async def usersclass(id: int):#Esta variable tiene que ser la misma que en la línea 57
    users = filter(lambda user: user.Celid == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
