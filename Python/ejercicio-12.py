# 12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

frase = "El mejor lenguaje de todos para programar es Python".split()
longitudes = list(map(len, frase))

print(longitudes)