# 23. Concatena una lista de palabras. Usa la función reduce().

from functools import reduce

frase = reduce(lambda x, y: x + " " + y, ["Casa", "Armario", "Perro", "Ordenador"])
print(frase)