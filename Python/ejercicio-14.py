# 14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

palabras_con_a = list(filter(lambda palabra:  palabra.upper().startswith('A'), ["Ana", "Juan", "Alvaro", "Zoo", "araña"]))
print(palabras_con_a)