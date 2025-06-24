# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

lista_variada = [("Maria", "Pablo"), ("Paco","Pepe"), ("Juan", "Lucia")]
cadena_texto = ",".join(list(map(lambda x: ",".join(x), lista_variada)))
nueva_lista = cadena_texto.split(",")
print(nueva_lista)