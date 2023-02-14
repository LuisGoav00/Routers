#en vez de importar el framework, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel #Importamos pydantic para obtener una entidad que pueda definir usuarios


router = APIRouter()
#en vez de fastapi: con APIRouter

#Definimos nuestra entidad User (utilizando BaseModel):
class User (BaseModel):
    Matricula:int
    Nombre:str
    Carrera:str

users_list=  [
User(Matricula=201925487,Nombre="Pedro",Carrera="ITI"),
User(Matricula=201954786,Nombre="Juan",Carrera="Ingenieria Civil"),
User(Matricula=201754862,Nombre="Alberto",Carrera="Arquitectura")   
]

@router.get("/estudiantes/", status_code=status.HTTP_200_OK)
async def estudiantes():
    return users_list

#Función Get con Filtro Path
@router.get("/estudiantes/{id}",status_code=status.HTTP_200_OK)
async def usersclass(id: int):#Esta variable tiene que ser la misma que en la línea 57
    users = filter(lambda user: user.Matricula == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
