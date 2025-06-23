""" 
3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original que contengan 
la palabra objetivo.
"""

def filtrar_por_subcadena(lista, subcadena_objetivo):
    return [palabra for palabra in lista if subcadena_objetivo in palabra]

palabras = ['jardin','luz','perro','messi','ventana','pajaro','mes','mesopotamia','arbol','demuestra', 'muestra','mesera','enmesar','gato','tremesura','casa','remeson']
objetivo = 'mes'

lista = filtrar_por_subcadena(palabras, objetivo)
print(lista)
