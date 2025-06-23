""" 
13. Genera una función que, para un conjunto de caracteres, 
devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
Las letras no pueden estar repetidas. Usa la función map().
"""

def duplicar_caracteres(l):
    return (l.upper(), l)

tupla = sorted(map(duplicar_caracteres, set("abbbcadefffghosjfklmmmnipqerrrstuvwxyz")))
print(tupla)