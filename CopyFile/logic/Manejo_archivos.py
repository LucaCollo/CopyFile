import shutil
from clases.Carpeta import Carpeta
from clases.Tarea import Tarea
from threading import Timer



def establecerCarpetaOrigen():
    rutaCarpetaOrigen = input("Ingrese la ruta de la carpeta de origen:  ")
    return rutaCarpetaOrigen

def establecerCantidadArchivos():
    numArchivos = int(input("Cuántos archivos quiere trasladar?  "))
    return numArchivos

def establecerCarpetaDestino():
    rutaCarpetaDestino = input("Ingrese la carpeta de destino de los archivos:  ")
    return rutaCarpetaDestino


# Bitácora
# Se guarda tarea en memoria y se copia en otra carpeta
def creacionTareaYTrasladoArchivos():
    #info tarea
    idTarea = input("Ingrese id de la tarea: ")
    temporizador = float(input("Ingrese el tiempo a transcurir antes que se realice la tarea (en segundos): "))
    #info carpeta
    rutaCarpetaOrigen = establecerCarpetaOrigen()
    numArchivos = int(input("Ingrese la cantidad de archivos a trasladar:  "))

    listaNomArchivos =[] 
    for i in range(numArchivos):
        nombreArchivo = input(f"Cuál es el nombre del archivo {i+1} a trasladar?  ")
        listaNomArchivos.append(nombreArchivo) #se añade cada nombre de archivo en la listaNomArchivos

    #Crear la lista de las rutas de los archivos a trasladar
    archivos = []
    for i in range (len(listaNomArchivos)):
        rutaArchivo = f"{rutaCarpetaOrigen}\{listaNomArchivos[i]}" 
        archivos.append(rutaArchivo)#se añade cada ruta de archivo a trasladar en la lista archivos

    rutaCarpetaDestino = establecerCarpetaDestino()

    #creación de objetos carpetas
    carpetaOrigen = Carpeta (rutaCarpetaOrigen, len(listaNomArchivos), listaNomArchivos)
    carpetaDestino = Carpeta (rutaCarpetaDestino, 0, {})
    #creación de objeto tarea
    tarea = Tarea(idTarea, temporizador, carpetaOrigen, carpetaDestino)
    #Creación de método para mover archivos en otra función. Esto dado a que la clase Timer necesita del nombre de un método.
    def copiarArchivos():
        for i in range (len(archivos)):
        #shutil.move(archivos[i], rutaCarpetaDestino) #para mover
            shutil.copy(archivos[i], rutaCarpetaDestino)
    #Funcionalidad principal de traslado de archivos
    timer = Timer(temporizador, copiarArchivos)
    timer.start()

    return tarea



#Añadir tarea a la bitacora.txt->en el archivo Registro_info

#Ver info de bitacora.txt
def verBitacora():
    with open(r"C:\Users\lucac\Desktop\UIA\UIA - Progra 2\Prueba 1\bitacora.txt","r") as archivo:
        for linea in archivo:
            print(linea)


#Filtrar archivos por tipo de archivos
def filtrarArchivos():
    print("Está función todavía no está implementada")