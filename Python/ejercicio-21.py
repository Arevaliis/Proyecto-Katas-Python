# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

numero = int(input("Introduce un numero: "))
cubo = lambda x: x ** 3

print(f"El cubo de {numero} es igual a {cubo(numero)}")