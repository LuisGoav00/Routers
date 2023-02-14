#en vez de importar el framework, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel #Importamos pydantic para obtener una entidad que pueda definir usuarios


router = APIRouter()
#en vez de fastapi: con APIRouter

#Definimos nuestra entidad User (utilizando BaseModel):
class User (BaseModel):
    Empleadoid:int
    Puesto:str
    Sueldo:int

users_list=  [
User(Empleadoid=1,Puesto="Jefe",Sueldo="10000"),
User(Empleadoid=2,Puesto="Chalan",Sueldo="5000"),
User(Empleadoid=3,Puesto="Chofer",Sueldo="6000")   
]

@router.get("/empleados/", status_code=status.HTTP_200_OK)
async def empleados():
    return users_list

#Función Get con Filtro Path
@router.get("/empleados/{id}",status_code=status.HTTP_200_OK)
async def usersclass(id: int):#Esta variable tiene que ser la misma que en la línea 57
    users = filter(lambda user: user.Empleadoid == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
