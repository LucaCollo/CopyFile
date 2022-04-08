from clases.Carpeta import Carpeta

# Esta clase define el estado y el comportamiento de una tarea
class Tarea(Carpeta):  #Tarea y Carpeta tienen una relación de asociación debido a que Tarea necesita a Carpeta sin embargo no existe ninguna relación de suboordinación por parte de Carpeta. (https://virtual.itca.edu.sv/Mediadores/ads/213_tipos_de_relaciones.html)

    # Método constructor
    def __init__(self, idTarea, fechaCreacion, tipoArchivos, temporizador, carpetaOrigen, carpetaDestino): #Atributos
        # Atributos de instancia
        self._idTarea = idTarea
        self._fechaCreacion = fechaCreacion
        self._tipoArchivos = tipoArchivos
        self._temporizador = temporizador
        self._carpetaOrigen = carpetaOrigen
        self._carpetaDestino = carpetaDestino

    # Métodos get y set para print y modificar
    @property
    def idTarea(self):
        return self._idTarea
        
    @idTarea.setter
    def idTarea(self, idTarea):
        self._idTarea = idTarea

    @property
    def fechaCreacion(self):
       return self._fechaCreacion
        
    @fechaCreacion.setter
    def idCarpeta(self, fechaCreacion):
       self._fechaCreacion = fechaCreacion

    @property
    def tipoArchivos(self):
        return self._tipoArchivos
        
    @idTarea.setter
    def tipoArchivos(self, tipoArchivos):
        self._tipoArchivos = tipoArchivos
    
    

    @property
    def temporizador(self):
        return self._temporizador
        
    @temporizador.setter
    def temporizadora(self, temporizador):
        self._temporizador = temporizador


     # Método str
    def __str__(self):
        return f"\n\nTarea#{self.idTarea} Fecha de creación:{self.fechaCreacion} \n Tipos de archivos a transferir: {self._tipoArchivos} \n Tiempo hasta que se realice la tarea: {self.temporizador} segundos \n Carpeta origen: {self._carpetaOrigen} \n Carpeta destino: {self._carpetaDestino}"

    # Método repr -> igual que str pero sirve para mostrar la info de un objeto al agregarlo a un arreglo. Sino solo se muestra el id del objeto
    def __repr__(self):
        return f"\n\nTarea#{self.idTarea} \n Fecha de creación:{self.fechaCreacion} \n Tipos de archivos a transferir: {self._tipoArchivos} \n Tiempo hasta que se realice la tarea: {self.temporizador} segundos \n Carpeta origen: {self._carpetaOrigen} \n Carpeta destino: {self._carpetaDestino}"
        

