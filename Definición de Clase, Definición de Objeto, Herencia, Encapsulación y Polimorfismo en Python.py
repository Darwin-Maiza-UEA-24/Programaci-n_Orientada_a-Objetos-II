""" Definición de Clase, Definición de
    Objeto, Herencia, Encapsulación y Polimorfismo en Python"""
class Animal:

    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación: atributo privado

    def hacer_sonido(self):
        print("El animal hace un sonido")

    def obtener_nombre(self):
        return self.__nombre

class Perro(Animal):
    """Clase derivada que representa a un perro"""

    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    """Clase derivada que representa a un gato"""

    def hacer_sonido(self):
        print("Miau!")

# Polimorfismo:
def hacer_sonar_animal(animal):
    animal.hacer_sonido()

# Creando objetos
perro = Perro("Firulais")
gato = Gato("Michi")

# Utilizando los objetos
perro.hacer_sonido()  # Salida: Guau!
gato.hacer_sonido()  # Salida: Miau!

# Demostrando polimorfismo
hacer_sonar_animal(perro)
hacer_sonar_animal(gato)