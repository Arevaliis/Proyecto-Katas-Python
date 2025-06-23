# 39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, parametros):
    match figura[0].upper().strip():
        case "R":
            base, altura = parametros
            print(f"El area del rectangulo es de {base * altura}")
        case "C":
            radio = parametros[0]
            print(f"El area del circulo es {round(math.pi * (radio ** 2), 2)}")
        case "T":
            base, altura = parametros
            print(f"El area del triangulo es de {(base * altura / 2)}")
        case _:
            print("Has introducido mal los parametros o la figura")

try:
    datos_circulo = (int(input("Ingrese el Radio del Circulo: ")), )
    calcular_area("Circulo", datos_circulo)
    print("------------------------------")
    datos_rectangulo = (int(input("Ingrese la base del Rectángulo:" )), int(input("Ingrese la altura del Rectángulo: "))) 
    calcular_area("Rectangulo", datos_rectangulo)
    print("------------------------------")
    datos_triangulo = (int(input("Ingrese la base del Triángulo:" )), int(input("Ingrese la altura del Triángulo: "))) 
    calcular_area("Triangulo", datos_triangulo)
except ValueError:
    print("Debe introducir solo numeros")