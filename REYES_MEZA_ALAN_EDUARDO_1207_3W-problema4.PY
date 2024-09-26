print(" ")  # ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR
print("# REYES MEZA ALAN EDUARDO : EXAMEN PRIMER PARCIAL act4 # NOMBRE DE ACTIVIDAD Y DATOS DEL PROGRAMADOR")
print(" ")

# Lectura de los valores desde el teclado
A = float(input("Ingrese el primer valor (A): ")) # leer valor de A
B = float(input("Ingrese el segundo valor (B): ")) # leer valor de B
C = float(input("Ingrese el tercer valor (C): ")) # leer valor de C

print(" ")

if A == B or B == C or A == C: # Verificar que los valores sean distintos
    print("AVISO: Los valores ingresados deben ser distintos.")
else:
    print(" ")
    mayor = max(A, B, C) # sacar la letra mayor
    menor = min(A, B, C) # sacar la letra menor

    print(f"El mayor valor es: {mayor}") # Imprimir los resultados
    print(f"El menor valor es: {menor}") # Imprimir los resultados


