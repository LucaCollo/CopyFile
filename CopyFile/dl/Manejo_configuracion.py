import time

def leerConf():
    archivo = open("configuracion.txt", "rt")
    listaConfiguracion = archivo.read()
    listaConfiguracion = listaConfiguracion.splitlines()
    return listaConfiguracion

def verConf():
    print(f"\nConfiguración:\n")
    with open("configuracion.txt","rt") as archivo:
        for linea in archivo:
            print(linea)

def borrarConf():
    with open("configuracion.txt", 'r+') as archivo:
        archivo.truncate(0)
        print("Borrando la configuración en:")
        time.sleep(2)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Se ha borrado el contenido del archivo configuración!")