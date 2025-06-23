# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

lista_variada = [("Maria", "Pablo"), ("Paco","Pepe"), ("Juan", "Lucia")]
nueva_lista = list(map(lambda x: x, lista_variada))
print(nueva_lista)