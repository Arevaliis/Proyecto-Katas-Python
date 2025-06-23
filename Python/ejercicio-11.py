""" 
11. Escribe un programa que pida al usuario que introduzca su edad. 
Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado 
(por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
"""
def ingresar_edad(edad):
    if 0 < edad < 120:
        print(f"Tienes {edad} años")
    else:
        raise IndexError("Introduzca un numero mayor que 0 y menor que 120")

try:
    ingresar_edad(int(input("Introduzca su Edad: ")))
except IndexError as e:
    print(e)