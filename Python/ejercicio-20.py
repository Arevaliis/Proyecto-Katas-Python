# 20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

lista_variada = [5, "Sol", 4, "Pajaro", "Muro", 7, 8, 10]

numeros = list(filter(lambda x: isinstance(x, int), lista_variada))
print(numeros)