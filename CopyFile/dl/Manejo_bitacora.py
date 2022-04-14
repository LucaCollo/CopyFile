import time
#Ver info de bitacora.txt
def verBitacora():
    print(f"\nBitácora:")
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
        print("Se ha borrado la bitácora!")

#Añadir objeto tarea a la bitacora.txt
def guardarTarea(tarea):
    #Para guardar en txt cada nueva tarea que se crea # el archi es equivalente a la bitácora
    archivo=open("bitacora.txt","a+") #el a+ sirve para no sobreescribir lo que ya se ha añadido al documento txt. Se puede poner cualquier ruta
    archivo.write(str(tarea)) 
    archivo.close()
