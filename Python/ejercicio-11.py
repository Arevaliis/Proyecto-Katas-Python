""" 
11. Escribe un programa que pida al usuario que introduzca su edad. 
Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado 
(por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
"""
def ingresar_edad(edad):
    try: 
        if 0 < edad < 120:
            print(f"Tienes {edad} años")
        else:  
            raise IndexError("Error -> El numero debe ser mayor que 0 y menor que 120.")
    except IndexError as e:
        print(e)

ingresar_edad(int(input("Introduzca su Edad: ")))