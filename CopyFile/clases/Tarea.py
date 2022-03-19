from clases.Carpeta import Carpeta

# Esta clase define el estado y el comportamiento de una tarea
class Tarea(Carpeta):  #Tarea hereda Carpeta

    # Método constructor
    def __init__(self, idTarea, temporizador, carpetaOrigen, carpetaDestino): #Atributos
        # Atributos de instancia
        self._idTarea = idTarea
        #self._fechaCreacion = fechaCreacion
        self._temporizador = temporizador
        self._carpetaOrigen = carpetaOrigen
        self._carpetaDestino = carpetaDestino
        #listaNomArchivos.__init__(self, listaNomArchivos)# Atributo de clase

    # Métodos get y set para print y modificar
    @property
    def idTarea(self):
        return self._idTarea
        
    @idTarea.setter
    def idCarpeta(self, idTarea):
        self._idTarea = idTarea
    
    #@property
    #def fechaCreacion(self):
    #    return self._fechaCreacion
        
    #@fechaCreacion.setter
    #def idCarpeta(self, fechaCreacion):
    #    self._fechaCreacion = fechaCreacion

    @property
    def temporizador(self):
        return self._temporizador
        
    @temporizador.setter
    def temporizadora(self, temporizador):
        self._temporizador = temporizador


     # Método str
    def __str__(self):
        return f"\n\nTarea#{self.idTarea}\n Tiempo hasta que se realice la tarea: {self.temporizador} segundos \n Carpeta origen: {self._carpetaOrigen} \n Carpeta destino: {self._carpetaDestino}"

    # Método repr -> igual que str pero sirve para mostrar la info de un objeto al agregarlo a un arreglo. Sino solo se muestra el id del objeto
    def __repr__(self):
        return f"\n\nTarea#{self.idTarea}\n Tiempo hasta que se realice la tarea: {self.temporizador} segundos \n Carpeta origen: {self._carpetaOrigen} \n Carpeta destino: {self._carpetaDestino}"
    



