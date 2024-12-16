# Tecnicas de Programación
                                  # Abstracción
#La abstracción es el proceso de ocultar los detalles de implementación
# y mostrar solo la funcionalidad esencial del objeto.
# Permite que el usuario interactúe con el sistema sin preocuparse por la complejidad interna.

#Imaginar que estamos trabajando con una clase Vehículo.
# No necesitamos saber cómo funciona el motor internamente,
# sino que solo necesitamos las funciones que permiten a un vehículo moverse.
from abc import ABC, abstractmethod

# Clase base abstracta
class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

# Clase derivada que implementa el método abstracto
class Coche(Vehiculo):
    def mover(self):
        return "El coche está moviéndose"

class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta está pedaleando"

# Usando las clases
vehiculo1 = Coche()
vehiculo2 = Bicicleta()

print(vehiculo1.mover())  # El coche está moviéndose
print(vehiculo2.mover())  # La bicicleta está pedaleando


                                      #Encapsulación
# La encapsulación es el concepto de ocultar los detalles internos de los objetos
# y solo exponer lo necesario para interactuar con ellos.
# Se logra usando métodos de acceso como getters y setters.

class CuentaBancaria:
    def __init__(self, balance):
        self.__balance = balance  # Atributo privado

    # Getter
    def obtener_balance(self):
        return self.__balance

    # Setter
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__balance += cantidad
        else:
            print("Depósito no válido")

    def retirar(self, cantidad):
        if cantidad <= self.__balance:
            self.__balance -= cantidad
        else:
            print("Fondos insuficientes")

# Usando la clase
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)

print(cuenta.obtener_balance())  # 1200


                                # Herencia
#La herencia permite que una clase derive o herede características
# y comportamientos de otra clase.
# Esto permite reutilizar código y establecer jerarquías entre clases.

# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido.")


# Clase derivada (hereda de Animal)
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor de la clase base
        self.raza = raza

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")


# Usando las clases
animal = Animal("Animal genérico")
perro = Perro("Rex", "Labrador")

animal.hacer_sonido()  # El animal hace un sonido.
perro.hacer_sonido()  # Rex dice: ¡Guau!


                                       # Polimorfismo
# El polimorfismo permite que diferentes clases tengan métodos con el mismo nombre,
# pero con comportamientos diferentes.
# El polimorfismo se logra generalmente a través de la herencia y la sobrescritura de métodos.

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase.")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace: ¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace: ¡Miau!")

# Usando polimorfismo
def hacer_sonido_del_animal(animal: Animal):
    animal.hacer_sonido()

# Crear instancias
perro = Perro()
gato = Gato()

# Llamar al mismo método pero con diferentes comportamientos
hacer_sonido_del_animal(perro)  # El perro hace: ¡Guau!
hacer_sonido_del_animal(gato)   # El gato hace: ¡Miau!