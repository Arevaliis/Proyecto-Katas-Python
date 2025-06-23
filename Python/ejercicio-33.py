# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

suma_listas = lambda x, y: x + y
lista_sumanda = list(map(suma_listas, [1,2,3,4], [1,2,3,4]))
print(lista_sumanda)