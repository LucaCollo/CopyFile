import time
#Ver info de bitacora.txt
def verBitacora():
    with open("bitacora.txt","rt") as archivo:
        for linea in archivo:
            print(linea)

def borrarBitacora():
    with open("bitacora.txt", 'r+') as archivo:
        archivo.truncate(0)
        print("Borrando bitácora en:")
        time.sleep(2)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Se ha borrado la bitácora exitosamente!")