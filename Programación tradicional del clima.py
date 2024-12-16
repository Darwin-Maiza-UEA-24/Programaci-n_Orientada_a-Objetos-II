#Programación Tradicional
# Función para ingresar las temperaturas de los 7 días de la semana
def Digitar_temperaturas():
    # Aqui la lista vacía donde se almacenarán las temperaturas diarias
    temperaturas = []

    # Se crea un ciclo que repite 7 veces por cada día de la semana se coloca uno
    for i in range(1, 8):
        while True:  # Bucle para garantizar que se ingrese un valor válido
            try:
                # Solicitar al usuario digitar la temperatura para el día i
                temp = float(input(f"Ingrese la temperatura del día {i}: "))
                # se añade la temperatura a la lista de abajo
                temperaturas.append(temp)
                break  # Salimos del bucle si la entrada es válida
            except ValueError:
                # Cuando el usuario digita algo que no es un número, muestrar un error
                print("Favor, ingresar un valor numérico válido.")

    return temperaturas  # Se  Devuelve la lista de temperaturas


# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    # Se suman todas las temperaturas y se dividen entre 7 (que es el número de días)
    return round(sum(temperaturas) / len(temperaturas), 2)  # Redondeamos el resultado a 2 decimales

# La función para mostrar el resultado final
def mostrar_resultado(promedio):
    # Se Muestra el promedio de las temperaturas de la semana
    print(f"La temperatura promedio para la semana es: {promedio}°C")


# Función principal que organiza la ejecución del programa
def main():
    print("Cálculo del Promedio Semanal de Temperaturas")  # Mensaje introductorio
    temperaturas = Digitar_temperaturas()  # Llamamos a la función para ingresar las temperaturas
    promedio = calcular_promedio(temperaturas)  # Se realiza el calculo del promedio de las temperaturas
    mostrar_resultado(promedio)  # Mostrando el resultado al usuario


# Ejecución del programa si archivo es el principal
if __name__ == "__main__":
    main()
                                    # Programación Tradicional:
# De esta forma se utiliza funciones para organizar el código y realizar
  # las tareas necesarias esenciales: entrada de datos y cálculo del promedio.
# La función Digitar_temperaturas() utiliza un ciclo for para pedir las temperaturas de 7 días.
# Cada temperatura se guarda en una lista.
# Si el usuario ingresa un valor no numérico, el programa solicita la entrada nuevamente usando un ciclo while con manejo de excepciones.
# Cálculo del promedio: La función calcular_promedio() toma la lista de temperaturas,
# La suma de todos los valores y la divide entre 7, que es el número de días. El resultado se redondea a dos decimales.
# Se muestra resultados: La función mostrar_resultado() muestra el promedio calculado al usuario.
# El código está dividido en funciones, lo que mejora la organización y facilita la lectura del código.

# 1.- Programación Tradicional puede ser más sencilla para programas pequeños,
# pero a medida que el proyecto crece, puede ser difícil de mantener y escalar.
# 2.- En Programación Tradicional, las funciones se usan para estructurar el flujo de control.
# 3.- En Programación Tradicional, los datos (temperaturas) son gestionados directamente dentro de las funciones.

# Ambos enfoques son válidos, pero la Programación Orientada a Objetos ofrece una solución más robusta y flexible
# especialmente a medida que los programas crecen en complejidad.
# La Programación Tradicional puede ser más fácil de entender y utilizar para problemas pequeños y simples.