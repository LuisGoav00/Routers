#en vez de importar el framework, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel #Importamos pydantic para obtener una entidad que pueda definir usuarios


router = APIRouter()
#en vez de fastapi: con APIRouter

#Definimos nuestra entidad User (utilizando BaseModel):
class User (BaseModel):
    Posicion:str
    Titular:str
    Deporte:str

users_list=  [
User(Posicion="Filder",Titular="Si",Deporte="Beisbol"),
User(Posicion="Defensa",Titular="No",Deporte="Futbol"),
User(Posicion="Pitcher",Titular="No",Deporte="Beisbol")   
]

@router.get("/jugadores/", status_code=status.HTTP_200_OK)
async def jugadores():
    return users_list
