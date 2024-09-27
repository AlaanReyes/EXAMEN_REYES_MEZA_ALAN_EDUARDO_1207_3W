print(" ")  # ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR
print("# REYES MEZA ALAN EDUARDO : EXAMEN PRIMER PARCIAL act6 # NOMBRE DE ACTIVIDAD Y DATOS DEL PROGRAMADOR")
print(" ")

# Solicitar al usuario que ingrese un número 
try:
    # Convertir la entrada del usuario a un número 
    numero = int(input("Ingresa un número : "))

    if numero > 40: # Verificar si el número es mayor a 40
        if numero % 7 == 0: # Verificar si el número es divisible por 7

            print(f"El número {numero} es mayor a 40 y es divisible por 7.") # Si ambas condiciones se cumplen, mostrar si es mayor que 40
        else:
            print(f"El número {numero} es mayor a 40, pero NO es divisible por 7.") # Si no es divisible por 7, mostrar un mensaje indicando eso
    else:
        print(f"El número {numero} NO es mayor a 40.")# Si no es mayor a 40, mostrar un mensaje indicando eso

except ValueError: #mostrar errores si los hay
    print("Por favor, ingresa un número entero válido.") # Informar al usuario que debe ingresar un número entero válido
