print(" ")  # ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR
print("# REYES MEZA ALAN EDUARDO : EXAMEN PRIMER PARCIAL act6 # NOMBRE DE ACTIVIDAD Y DATOS DEL PROGRAMADOR")
print(" ")

# calcular el factorial de un numero
def factorial(n):
    resultado = 1  # Iniciamos el resultado en 1
    for i in range(1, n + 1): #  multiplicamos desde n hasta 1
        resultado *= i  # Multiplicamos el resultado por el numero actual
    return resultado  # Devolvemos el resultado final

# Solicitar al usuario que ingrese un numero entero no negativo
try:
    numero = int(input("Ingresa un numero entero no negativo: "))

    if numero < 0: # Verificar si el número es negativo
        print("Por favor, ingresa un numero entero no negativo.") #ingresar un numero NO negativo
    else:
        resultado_factorial = factorial(numero)  #usar la función factorial y almacenar el resultado
        print(f"El factorial de {numero} es: {resultado_factorial}") # Mostrar el resultado del factorial en pantalla 

except ValueError: #buscar errores si los hay
    print("Por favor, ingresa un numero valido.") # ERROR, ingresar un numero valido
