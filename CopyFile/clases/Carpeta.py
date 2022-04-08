
# Esta clase define el estado y el comportamiento de una carpeta
class Carpeta:

    # Método constructor
    def __init__(self, rutaCarpeta,listaArchivos):#
        # Atributos de instancia
        self.rutaCarpeta = rutaCarpeta
        self.listaNomArchivos = listaArchivos

    # Métodos get y set para print y modificar
    @property
    def rutaCarpeta(self):
        return self._rutaCarpeta
        
    @rutaCarpeta.setter
    def rutaCarpeta(self, rutaCarpeta):
        self._rutaCarpeta = rutaCarpeta
    
    @property
    def listaArchivos(self):
        return self._listaArchivos
        
    @listaArchivos.setter
    def listaNomArchivos(self, listaArchivos):
        self._listaArchivos = listaArchivos

        
    # Método str
    def __str__(self):
        return f"\n Ruta: {self.rutaCarpeta}  \n Lista de archivos: {self.listaArchivos}"

    # Método repr -> igual que str pero sirve para mostrar la info de un objeto al agregarlo a un arreglo. Sino solo se muestra el id del objeto
    def __repr__(self):
        return f"\n Ruta: {self.rutaCarpeta}  \n Lista de archivos: {self.listaArchivos}"




    
