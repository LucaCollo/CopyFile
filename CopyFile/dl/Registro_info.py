import logic.Manejo_archivos as ma

#Añadir objeto tarea a la bitacora.txt
def guardarTarea():
    tarea= ma.creacionTareaYTrasladoArchivos()
    #Para guardar en txt cada nueva tarea que se cree  # el archi es equivalente a la bitácora
    archi=open(r"C:\Users\lucac\Desktop\UIA\UIA - Progra 2\Prueba 1\bitacora.txt","a+") #el a+ sirve para no sobreescribir lo que ya se ha añadido al documento txt. Se puede poner cualquier ruta
    archi.write(str(tarea)) 
    archi.close()


