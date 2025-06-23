# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

def diferencia(x, y):
    return x - y

lista = list(map(diferencia, [2,4,6,8], [0,6,1,3]))
print(lista)