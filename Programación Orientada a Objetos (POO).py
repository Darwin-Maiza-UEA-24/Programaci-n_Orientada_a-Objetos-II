#Programación Orientada a Objetos (POO)
#En esta forma se crea una clase que encapsula la información de las temperaturas diarias
# y proporciona métodos para ingresar los datos y calcular el promedio.
class Clima:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio de las temperaturas
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Clase principal
def main():
    print("Programa para calcular el promedio semanal del clima usando POO.")
    clima = Clima()  # Crear una instancia de la clase Clima
    clima.ingresar_temperaturas()  # Ingresar las temperaturas
    promedio = clima.calcular_promedio()  # Calcular el promedio
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
                            # Programación Orientada a Objetos (POO)
# Explicación
#(Clima) Es una clase que tiene un atributo temperaturas para almacenar las temperaturas diarias.
# Tiene dos métodos:
#(ingresar_temperaturas) Solicita las temperaturas diarias al usuario y las agrega a la lista temperaturas
#(calcular_promedio) Calcula el promedio de las temperaturas de la semana.
#(main) Crea una instancia de la clase Clima, solicita los datos y calcula el promedio semanal

# 1.- En POO, el código está organizado en torno a objetos y clases.
# La lógica está encapsulada dentro de una clase, lo que mejora la reutilización y la organización.
# 2.- En POO, la reusabilidad está mejor soportada mediante las clases.
# se puede crear objetos de la misma clase y reutilizar métodos fácilmente,
# y también se puede extender la funcionalidad mediante herencia.
#POO facilita la escalabilidad, ya que puedes extender clases, agregar nuevas funcionalidades
# y modificar la lógica sin afectar otras partes del código.


# Ambos enfoques son válidos, pero la Programación Orientada a Objetos ofrece una solución más robusta y flexible
# especialmente a medida que los programas crecen en complejidad.
# La Programación Tradicional puede ser más fácil de entender y utilizar para problemas pequeños y simples.
