#########################################Primera Parte################################################
# Instalación del framwork fastApi, código:
# -pip install fastapi-

#Instalación del Servidor Uvicorn, código:
#-pip install "uvicorn[standard]"-

# Instalación del framwork fastApi, código:
# -pip install fastapi[all]-

#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI
#Importamos de la carpeta "routers" los archivos "router1" y "router1_2"
from routers import routers1, routers1_2, routers1_3, routers1_4, routers1_5, routers1_6, routers1_7, routers1_8, routers1_9, routers1_10
#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Creamos un router a partir de la class router1
app.include_router(routers1.router)

#Creamos un router a partir de la class router1_2
app.include_router(routers1_2.router)

app.include_router(routers1_3.router)

app.include_router(routers1_4.router)

app.include_router(routers1_5.router)

app.include_router(routers1_6.router)

app.include_router(routers1_7.router)

app.include_router(routers1_8.router)

app.include_router(routers1_9.router)

app.include_router(routers1_10.router)




#Creamos un router a partir de la class router1_3
app.include_router(routers1.router)

#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/")

#creamos la función asincrona "imprimir"
async def imprimir():
    return "Hola estudiantes"


#Levantamos el server Uvicorn
#-uvicorn main:app --reload-
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000

#########################################Segunda Parte################################################

#creamos la función asincrona con formato JSON
@app.get("/Git")
async def imprimir():
    return {"Git_curso":"https://github.com/freddy-7777/Modelos-de-desarrollo-WEB.git"}

# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/Git


##################CLASE 3################

#Detener server con: ctrl + c

#Documentación con Swagger: http://127.0.0.1:8000/docs
#Documentación con Redocly: http://127.0.0.1:8000/redoc
