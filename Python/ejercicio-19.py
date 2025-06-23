# 19. Crea una función lambda que filtre los números impares de una lista dada.

numeros_impares = list(filter(lambda x: x % 2 != 0, [2,3,4,6,8,9]))
print(numeros_impares)