print(" ")  # ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR
print("# REYES MEZA ALAN EDUARDO : EXAMEN PRIMER PARCIAL act6 # NOMBRE DE ACTIVIDAD Y DATOS DEL PROGRAMADOR")
print(" ")

# Solicitar al usuario que ingrese un numero 
try:
    numero = int(input("Ingresa un número natural: ")) #pedir que se ingrese un numero
    if numero < 0: # Verificar si el número es menor que 0
        print("Por favor, ingresa un número natural válido (0 o positivo).") # Si el número es negativo, informar al usuario que debe ingresar un número natural válido
    else:
        if numero % 2 == 0:# Verificar si el número es par 
            print(f"El número {numero} es par.") # Si el resultado es 0, el número es par
        else:
            print(f"El número {numero} es impar.")# Si el resultado no es 0, el número es impar

except ValueError:# Capturar errores en caso de que se produzca un error 
    print("Por favor, ingresa un número natural válido.") # Informar al usuario que debe ingresar un número valido
