#Menú principal
import time
import logic.Manejo_bitacora as mb
import dl.Registro_info as ri

def escogerOpcion():
    print("-----------------------------------------")
    print("1. Programar el traslado de archivo")
    print("2. Ver la bitácora")
    print("3. Borrar bitácora")
    print("0. Salir del programa")
    opcion = int(input("Escoja una opción:"))
    return opcion


def activarOpcion():
    salir= False
    opcionMenu = escogerOpcion()
    while not salir:
        try:
            if(opcionMenu == 1):
                ri.guardarTarea()
                activarOpcion()
                break
            elif(opcionMenu == 2):
                mb.verBitacora()#ya lo pude hacer, solo que se imprime un toque raro
                activarOpcion()
                break
            elif(opcionMenu == 3):
                mb.borrarBitacora()
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
    

#Métodos
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


