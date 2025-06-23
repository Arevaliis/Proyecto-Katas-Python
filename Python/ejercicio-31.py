# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. 
# Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

def buscar_nombre(lista, nombre):
    if nombre in lista:
        print(f"El nombre {nombre.title()} se encuentra en la lista")
    else:
        raise ValueError(f"El nombre '{nombre.title()}' no se encuentra en la lista.")

try:
    nombres = input("Ingrese una lista de nombres separados por espacios: ").upper().strip()
    lista_nombres = nombres.split()
    nombre = input("Introduzca el nombre a buscar: ").upper().strip()
    buscar_nombre(lista_nombres, nombre)
except ValueError as e:
    print(e)