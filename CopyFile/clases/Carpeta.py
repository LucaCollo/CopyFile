
# Esta clase define el estado y el comportamiento de una carpeta
class Carpeta:

    # Método constructor
    def __init__(self, rutaCarpeta,  cantArchivos, listaNomArchivos):#
        # Atributos de instancia
        self.rutaCarpeta = rutaCarpeta
        self.cantArchivos = cantArchivos
        self.listaNomArchivos = listaNomArchivos

    # Métodos get y set para print y modificar
    @property
    def rutaCarpeta(self):
        return self._rutaCarpeta
        
    @rutaCarpeta.setter
    def rutaCarpeta(self, rutaCarpeta):
        self._rutaCarpeta = rutaCarpeta

    @property
    def cantArchivos(self):
        return self._cantArchivos
        
    @cantArchivos.setter
    def cantArchivos(self, cantArchivos):
        self._cantArchivos = cantArchivos
    
    @property
    def listaNomArchivos(self):
        return self._listaNomArchivos
        
    @listaNomArchivos.setter
    def listaNomArchivos(self, listaNomArchivos):
        self._listaNomArchivos = listaNomArchivos

        
    # Método str
    def __str__(self):
        return f"\n Ruta: {self.rutaCarpeta} \n Cantidad de archivos a transferir: {self.cantArchivos} \n Lista de archivos: {self.listaNomArchivos}"

    # Método repr -> igual que str pero sirve para mostrar la info de un objeto al agregarlo a un arreglo. Sino solo se muestra el id del objeto
    def __repr__(self):
        return f"\n Ruta: {self.rutaCarpeta} \n Cantidad de archivos a transferir: {self.cantArchivos} \n Lista de archivos: {self.listaNomArchivos}"




    
