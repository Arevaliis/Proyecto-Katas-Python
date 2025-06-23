# 1. Escribe una función que reciba una cadena de texto como parámetro y 
# devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

from collections import Counter

def frecuencia_letra(palabra):
    return Counter(palabra.lower().replace(" ", ""))

diccionario_frecuencia = frecuencia_letra(' P a s a p a l a b r a ')
print(diccionario_frecuencia)