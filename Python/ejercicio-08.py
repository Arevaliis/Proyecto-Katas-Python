""" 
8. Escribe un programa que pida al usuario dos números e intente dividirlos. 
Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja 
esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
"""

def division(x, y):
    try: 
        resultado = int(x) / int(y)
        print(f"La division tuvo exito. {x}/{y} = {resultado}")
    except ValueError:
        print("INGRESE SOLO NUMEROS")
    except ZeroDivisionError:
        print("NO PUEDE DIVIDIR POR CERO")
division(input("Dividendo: "), input("Divisor: "))