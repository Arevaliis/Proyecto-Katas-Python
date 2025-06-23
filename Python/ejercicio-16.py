# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def mayor_que_n(cadena_texto, num):
    lista_palabras = cadena_texto.split()
    return list(filter(lambda x: len(x) > num, lista_palabras))

cadena_texto = "La casa de Paula tiene una piscina en el jardin"
palabras_mayores_que_n = mayor_que_n(cadena_texto, 4)
print(palabras_mayores_que_n)