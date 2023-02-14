#en vez de importar el framework, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel #Importamos pydantic para obtener una entidad que pueda definir usuarios


router = APIRouter()
#en vez de fastapi: con APIRouter

#Definimos nuestra entidad User (utilizando BaseModel):
class User (BaseModel):
    Pcid:int
    Marca:str
    Año:int

users_list=  [
User(Pcid=1,Marca="HP",Año="2012"),
User(Pcid=2,Marca="Alienware",Año="2020"),
User(Pcid=3,Marca="Lenovo",Año="2006")   
]

@router.get("/computadoras/", status_code=status.HTTP_200_OK)
async def computadoras():
    return users_list

#Función Get con Filtro Path
@router.get("/computadoras/{id}",status_code=status.HTTP_200_OK)
async def usersclass(id: int):#Esta variable tiene que ser la misma que en la línea 57
    users = filter(lambda user: user.Pcid == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
