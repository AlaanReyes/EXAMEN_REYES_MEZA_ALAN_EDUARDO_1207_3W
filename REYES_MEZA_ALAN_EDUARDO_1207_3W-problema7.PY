print(" ")  # ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR
print("# REYES MEZA ALAN EDUARDO : EXAMEN PRIMER PARCIAL act6 # NOMBRE DE ACTIVIDAD Y DATOS DEL PROGRAMADOR")
print(" ") #espacio


# Solicitar al usuario que ingrese un número natural
try:
    numero = int(input("Ingresa un número natural (1-12): ")) #pedir al usuario ingresar un numero

    # Verificar si el número está en el rango de 1 a 12
    if 1 <= numero <= 12:
        
        print(f"El número {numero} se encuentra dentro de la primera docena.") # imprimir si es que se encuentra 
        
        print(" ") #espacio
    else:
        
        print(f"El número {numero} NO está dentro de la primera docena.") # imprimir si no se encuentra 
       
        print(" ") #espacio
# Capturar error en caso de que se produzca un error de valor
except ValueError:
    print("Por favor, ingresa un número natural válido.") # Informar al usuario que debe ingresar un número natural válido
