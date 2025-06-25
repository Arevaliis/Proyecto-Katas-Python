# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

from functools import reduce

def calcular_factorial(numero):
    return reduce(lambda x,y: x * y, [num for num in range(1, numero +1)])

factorial_5 = calcular_factorial(5)
print(factorial_5)