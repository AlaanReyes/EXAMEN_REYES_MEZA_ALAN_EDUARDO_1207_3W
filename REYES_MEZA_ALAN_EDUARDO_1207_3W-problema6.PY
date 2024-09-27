print(" ")  # ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR
print("# REYES MEZA ALAN EDUARDO : EXAMEN PRIMER PARCIAL act6 # NOMBRE DE ACTIVIDAD Y DATOS DEL PROGRAMADOR")
print(" ")

# Definimos una función para calcular el área y el perímetro de un rectángulo
def calcular_rectangulo(base, altura):
    area = base * altura # Calculamos el área del rectángulo (base * altura)
    perimetro = 2 * (base + altura) # Calculamos el perímetro del rectángulo 2 * (base + altura)
    return area, perimetro  # Devolvemos el área y el perímetro como uno solo

try:
    base = float(input("Ingresa la base del rectángulo: ")) # Solicitamos al usuario que ingrese la base del rectángulo 
    
    print(" ") #espacio

    altura = float(input("Ingresa la altura del rectángulo: ")) # Solicitamos al usuario que ingrese la altura del rectángulo
    
    print(" ") #espacio
   
    area, perimetro = calcular_rectangulo(base, altura) #función para calcular rectangulo con la base y la altura proporcionadas

    print(f"El área del rectángulo es: {area}") # Mostramos el área del rectángulo en pantalla
    
    print(" ") #espacio
    
    print(f"El perímetro del rectángulo es: {perimetro}")  # Mostramos el perímetro del rectángulo en pantalla
    
    print(" ") #espacio

except ValueError: # Capturamos error en caso de que se produzca un error de valor
    print("Por favor, ingresa valores numéricos válidos.") # Informar al usuario que debe ingresar valores validos
