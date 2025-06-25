# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmarcarar_caracteres(palabra, caracter = "#"):
    return str(palabra).replace(palabra[:-4], (caracter * len(palabra[:-4]))) if type(palabra) == str else "Debe ingresar un String"

conversion1 = enmarcarar_caracteres("componente")
conversion2 = enmarcarar_caracteres("Nemo")
conversion3 = enmarcarar_caracteres(5)

print(conversion1)
print(conversion2)
print(conversion3)