#  Aplicación de Constructores (__init__) y destructores (__del__)

class Archivo:
    # Constructor: inicialización con los atributos del objeto
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase Archivo.
        Inicializa el atributo 'nombre_archivo' y abre el archivo en modo de escritura.
        """
        self.nombre_archivo = nombre_archivo
        print(f"[Pais] {self.nombre_archivo}")
        self.archivo = open(self.nombre_archivo, 'w')  # Abre el archivo para escribir

    # Método para escribir en el archivo
    def escribir(self, contenido):
        """
        Método para escribir contenido en el archivo.
        """
        if self.archivo:
            self.archivo.write(contenido + '\n')
            print(f"[Clima]: {contenido}")

    # Destructor: cierra el archivo cuando el objeto es destruido
    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se encarga de cerrar el archivo cuando el objeto es destruido.
        """
        if self.archivo:
            self.archivo.close()
            print(f"[Pais] El archivo {self.nombre_archivo} ha sido cerrado.")


# Ejemplo de uso de la clase Archivo

# Crear un objeto de la clase Archivo
archivo1 = Archivo("Ecuador")

# Escribir en el archivo
archivo1.escribir("Ecuador presenta diversos tipos de clima")
archivo1.escribir("Costa o Litoral, Sierra o Interandina, Oriente o Amazónica, Insular o Galápagos. ")

# El archivo se cierra automáticamente cuando el objeto se destruye (cuando el programa termina)
del archivo1  # Se llama explícitamente al destructor
