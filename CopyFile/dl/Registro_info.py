import shutil
import time
from clases.Carpeta import Carpeta
from clases.Tarea import Tarea
from threading import Timer
from datetime import datetime
import os

def establecerCarpetaOrigen():
    rutaCarpetaOrigen = input("Ingrese la ruta de la carpeta de origen:  ")
    return rutaCarpetaOrigen

def establecerCarpetaDestino():
    rutaCarpetaDestino = input("Ingrese la ruta de la carpeta de destino:  ")
    return rutaCarpetaDestino

def establecerArchivosATransferir():
    tipoArchivos = input("Ingrese los tipos de archivos a copiarse separados por espacios:  ").split()
    return tipoArchivos

# Se guarda tarea en memoria y se copia en otra carpeta
def copiarTarea():
    #info tarea
    idTarea = input("Ingrese id de la tarea: ")
    fechaCreacion = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    temporizador = float(input("Ingrese el tiempo a transcurir antes que se realice la tarea (en segundos): "))
    #info carpeta
    rutaCarpetaOrigen = establecerCarpetaOrigen()
    rutaCarpetaDestino = establecerCarpetaDestino()
    tipoArchivos = establecerArchivosATransferir()
    listaArchivosOrigen = os.listdir(rutaCarpetaOrigen)
    listaArchivosDestino = os.listdir(rutaCarpetaDestino)
    #creación de objetos carpetas
    carpetaOrigen = Carpeta (rutaCarpetaOrigen, listaArchivosOrigen)
    carpetaDestino = Carpeta (rutaCarpetaDestino, listaArchivosDestino)
    #creación de objeto tarea
    tarea = Tarea(idTarea, fechaCreacion, tipoArchivos, temporizador, carpetaOrigen, carpetaDestino)
    #Creación de método para mover archivos en otra función. Esto dado a que la clase Timer necesita del nombre de un método.
    def copiarArchivos():
            #Copiar archivos de una carpeta a otra según la configuración
        listaDocumentos = os.listdir(rutaCarpetaOrigen)
        for n in range(len(listaDocumentos)):
            for i in range(len(tipoArchivos)):
                if (listaDocumentos[n].endswith(tipoArchivos[i])):
                    rutaArchivo = f"{rutaCarpetaOrigen}\{listaDocumentos[n]}" 
                    shutil.copy(rutaArchivo,rutaCarpetaDestino)  #Comando para copiar elementos
    #Funcionalidad principal de traslado de archivos
    timer = Timer(temporizador, copiarArchivos)
    timer.start()
    time.sleep(2)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(f"Copiando archivos en {temporizador} segundos")
    return tarea

#Añadir objeto tarea a la bitacora.txt
def guardarTarea():
    tarea= copiarTarea()
    #Para guardar en txt cada nueva tarea que se cree  # el archi es equivalente a la bitácora
    archi=open("bitacora.txt","a+") #el a+ sirve para no sobreescribir lo que ya se ha añadido al documento txt. Se puede poner cualquier ruta
    archi.write(str(tarea)) 
    archi.close()

