print(" ")  # ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR
print("# REYES MEZA ALAN EDUARDO : EXAMEN PRIMER PARCIAL act5 # NOMBRE DE ACTIVIDAD Y DATOS DEL PROGRAMADOR")
print(" ") #espacio

def obtener_valores(): #ingresar valores 
    
    return float(input("Ingrese el primer valor: ")), float(input("Ingrese el segundo valor: ")) #ingresar valores

def menor_valor(val1, val2):
    """Devuelve el menor de dos valores."""
    return min(val1, val2) #devuelve al menor 

def sumar(val1, val2): #suma los valores 
    """Retorna la suma de dos valores."""
    return val1 + val2 #retorna la suma 

val1, val2 = obtener_valores() #obtener val1 y val2

print(" ") # espacio
print("El menor valor es:", menor_valor(val1, val2)) # saca el menor valor 

print(" ") #espacio
print("La suma es:", sumar(val1, val2)) # suma de los 2 valores 
print(" ") # espacio



