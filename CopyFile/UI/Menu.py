#Menú principal
import time
import dl.Manejo_bitacora as mb
import logic.Traslado_doc as li
import dl.Manejo_configuracion as conf

def escogerOpcion():
    print("-----------------------------------------")
    print("1. Trasladar archivos")
    print("2. Ver la bitácora")
    print("3. Borrar bitácora")
    print("4. Ver configuración")
    print("5. Borrar configuración")
    print("0. Salir del programa")
    opcion = int(input("Escoja una opción:"))
    return opcion


def activarOpcion():
    salir= False
    opcionMenu = escogerOpcion()
    while not salir:
        try:
            if(opcionMenu == 1):
                li.establecerDatos()
                activarOpcion()
                break
            elif(opcionMenu == 2):
                mb.verBitacora()
                activarOpcion()
                break
            elif(opcionMenu == 3):
                mb.borrarBitacora()
                activarOpcion()
                break
            elif(opcionMenu == 4):
                conf.verConf()
                activarOpcion()
                break
            elif(opcionMenu == 5):
                conf.borrarConf()
                activarOpcion()
                break
            elif(opcionMenu == 0):
                fin()
                salir = True
                break
            else:
                print("-----------------------------------------")
                print("¡Por favor digita una opción correcta!")
                activarOpcion()
                break
        except:
            print("Opción incorrecta")
    

#Salir del programa
def fin():
    print("¡Gracias por haber usado nuestro programa!")
    time.sleep(2)
    print("Cerrando programa en:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)


