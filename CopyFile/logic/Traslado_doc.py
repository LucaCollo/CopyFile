import shutil
import time
from clases.Carpeta import Carpeta
from clases.Tarea import Tarea
from threading import Timer
from datetime import datetime
import dl.Manejo_configuracion as conf
import dl.Manejo_bitacora as mb
import logging
import os

def establecerDatos():
    listaConfiguracion = conf.leerConf()
    listaInfo = []
    for i in range(len(listaConfiguracion)):
        listaLineaSplit= listaConfiguracion[i].split("=")
        listaInfo.append(listaLineaSplit[1].split(","))
    #Se cambia el nombre a cada info que necesitamos para que luego sean utilizadas en la copia y traslado de archivos
    idLote = listaInfo[0][0]
    rutaCarpetaOrigen = listaInfo[1][0]
    rutaCarpetaDestino = listaInfo[2][0]
    tipoArchivosCopy = listaInfo[3]#Tipo de archivos que ocupamos copiar
    tipoArchivosMove = listaInfo[4]#Tipo de archivos que ocupamos mover
    temporizador = float(listaInfo[5][0])
    indBitacora = listaInfo[6][0]
    listaArchivosOrigen = os.listdir(rutaCarpetaOrigen)
    listaArchivosDestino = os.listdir(rutaCarpetaDestino)
    #creación de objetos carpetas
    carpetaOrigen = Carpeta (rutaCarpetaOrigen, listaArchivosOrigen)
    carpetaDestino = Carpeta (rutaCarpetaDestino, listaArchivosDestino)

    #Traslado archivos
    def trasladoArchivos():
        try:
    #Copiar archivos de una carpeta a otra según la configuración
            for n in range(len(listaArchivosOrigen)):
                for i in range(len(tipoArchivosCopy)):
                    if (listaArchivosOrigen[n].endswith(tipoArchivosCopy[i])):
                        rutaArchivo = f"{rutaCarpetaOrigen}\{listaArchivosOrigen[n]}" 
                        shutil.copy(rutaArchivo,rutaCarpetaDestino)#Comando para copiar elementos
        

            #Mover archivos de una carpeta a otra según la configuración
            for n in range(len(listaArchivosOrigen)):
                for i in range(len(tipoArchivosMove)):
                    if (listaArchivosOrigen[n].endswith(tipoArchivosMove[i])):
                        rutaArchivo = f"{rutaCarpetaOrigen}\{listaArchivosOrigen[n]}" 
                        shutil.move(rutaArchivo,rutaCarpetaDestino) #Comando para mover elementos
        except OSError as Error:        
            print(Error.strerror)
        except BaseException:
            pass 
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
    logging.info(f"Thread %s: Iniciando tarea {idLote}....")                     
    logging.info(f"Hilo Principal(Main): antes de crear tarea {idLote} (thread)")
    logging.info(f"Hilo Principal(Main): antes de iniciar tarea {idLote} (thread)")
    timer = Timer(temporizador, trasladoArchivos)
    print("Empezando en:")
    time.sleep(2)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    timer.start()
    fechaCreacion = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    #creación de objeto tarea para ser registrado en la bitácora
    tarea = Tarea(idLote, fechaCreacion, carpetaOrigen, carpetaDestino, tipoArchivosCopy, tipoArchivosMove, temporizador, indBitacora)
    print(tarea)
    print(f"Copiando archivos en {temporizador} segundos")
    logging.info(f"Thread %s: Finalizando tarea {idLote}....")
    logging.info("Hilo Principal(Main): termino")
    # Redirige al método para guardar tarea
    if indBitacora == 'S':
        mb.guardarTarea(tarea)
    

