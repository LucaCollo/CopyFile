from clases.Carpeta import Carpeta

# Esta clase define el estado y el comportamiento de una tarea
class Tarea():  #Tarea y Carpeta tienen una relación de asociación debido a que Tarea necesita a Carpeta sin embargo no existe ninguna relación de suboordinación por parte de Carpeta. (https://virtual.itca.edu.sv/Mediadores/ads/213_tipos_de_relaciones.html)
    # Atributos de instancia
    idLote = 0
    fechaCreacion = ""
    carpetaOrigen = Carpeta
    carpetaDestino = Carpeta
    tiposArchivosCopy = ""
    tiposArchivosMove = ""
    temporizador = 0.0
    indBitacora = ""
    # Método constructor
    def __init__(self, idLote, fechaCreacion, carpetaOrigen, carpetaDestino, tipoArchivosCopy, tipoArchivosMove, temporizador, indBitacora):
        self._idLote = idLote
        self._fechaCreacion = fechaCreacion
        self._carpetaOrigen = carpetaOrigen
        self._carpetaDestino = carpetaDestino
        self._tipoArchivosCopy = tipoArchivosCopy
        self._tipoArchivosMove = tipoArchivosMove
        self._temporizador = temporizador
        self._indBitacora = indBitacora
        
    # Métodos get y set para print y modificar
    @property
    def idLote(self):
        return self._idLote
        
    @idLote.setter
    def idLote(self, idLote):
        self._idLote = idLote

    @property
    def fechaCreacion(self):
       return self._fechaCreacion
        
    @fechaCreacion.setter
    def idCarpeta(self, fechaCreacion):
       self._fechaCreacion = fechaCreacion

    @property
    def carpetaOrigen(self):
       return self._carpetaOrigen
        
    @carpetaOrigen.setter
    def carpetaOrigen(self, carpetaOrigen):
       self._carpetaOrigen = carpetaOrigen
    
    @property
    def carpetaDestino(self):
       return self._carpetaDestino
        
    @carpetaDestino.setter
    def carpetaDestino(self, carpetaDestino):
       self._carpetaDestino = carpetaDestino
    
    @property
    def tipoArchivosCopy(self):
       return self._tipoArchivosCopy
        
    @tipoArchivosCopy.setter
    def tipoArchivosCopy(self, tipoArchivosCopy):
       self._tipoArchivosCopy = tipoArchivosCopy
    
    @property
    def tipoArchivosMove(self):
       return self._tipoArchivosMove
        
    @tipoArchivosMove.setter
    def tipoArchivosMove(self, tipoArchivosMove):
       self._tipoArchivosMove = tipoArchivosMove
    
    @property
    def temporizador(self):
       return self._temporizador
        
    @temporizador.setter
    def temporizador(self, temporizador):
       self._temporizador = temporizador
    
    @property
    def indBitacora(self):
       return self._indBitacora
        
    @indBitacora.setter
    def indBitacora(self, indBitacora):
       self._indBitacora = indBitacora


     # Método str
    def __str__(self):
        return f"\nLote#{self.idLote} ({self.fechaCreacion})  \n Carpeta origen: {self.carpetaOrigen} \n Carpeta destino: {self.carpetaDestino} \n Tipos de archivos a copiar: {self.tipoArchivosCopy} \n Tipos de archivos a trasladar: {self.tipoArchivosMove} \n Tiempo hasta que se realice la tarea: {self.temporizador} segundos \n Indicador bitácora: {self.indBitacora}"

    # Método repr -> igual que str pero sirve para mostrar la info de un objeto al agregarlo a un arreglo. Sino solo se muestra el id del objeto
    def __repr__(self):
        return f"\nLote#{self.idLote} ({self.fechaCreacion})  \n Carpeta origen: {self.carpetaOrigen} \n Carpeta destino: {self.carpetaDestino} \n Tipos de archivos a copiar: {self.tipoArchivosCopy} \n Tipos de archivos a trasladar: {self.tipoArchivosMove} \n Tiempo hasta que se realice la tarea: {self.temporizador} segundos \n Indicador bitácora: {self.indBitacora}"
        

