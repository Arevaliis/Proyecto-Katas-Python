# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

lista_numeros = list(map(lambda x: x * 2, [2,4,6,8])) # Map nos devuelve la referencia del objeto en memoria, asi que debemos hacer un cast con list() para ver los valores.
print(lista_numeros)