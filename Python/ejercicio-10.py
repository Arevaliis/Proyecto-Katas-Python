""" 
10. Escribe una función que reciba una lista de números y calcule su promedio. 
Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
"""

def calcular_promedio(numeros):
    try:
        if not numeros:
            raise IndexError("Lista vacia")    
        print(f"El promedio es: {sum(numeros) / len(numeros)}")
    except IndexError as e:
        print(e)
    except TypeError:
        print("La lista solo puede contener numeros")   

calcular_promedio([2,3,4,5,6])
calcular_promedio(["2",5,6])
calcular_promedio([])