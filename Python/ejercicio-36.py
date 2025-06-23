""" 
36. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
    - contar_palabras, 
    - reemplazar_palabras 
    - eliminar_palabra.

Código a seguir:
    - Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
    - Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
    - Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
    - Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.

Caso de uso: Verificar el funcionamiento completo de procesar_texto.
"""

def procesar_texto(texto, accion):
    texto = texto.lower()
    lista_texto = texto.split()

    def contar_palabras():
        dicc_palabras = {}
        for palabra in lista_texto:
            if palabra not in dicc_palabras.keys():
                dicc_palabras[palabra] = texto.count(palabra)
        return dicc_palabras
    
    def remplazar_palabras():
        palabra_antigua = input("¿Que palabra quieres remplazar?: ").lower().strip()
        palabra_nueva = input("¿Palabra a usar?: ").lower().strip()
        return texto.replace(palabra_antigua, palabra_nueva).capitalize() if palabra_antigua in texto else f"No existe la palabra {palabra_antigua} dentro del texto"
    
    def eliminar_palabra():
        palabra_eliminada = input("¿Que palabra deseas eliminar del texto?: ").lower().strip()
        lista_texto.remove(palabra_eliminada)
        print("Palabra eliminada")
        return " ".join(lista_texto).capitalize()
                
    diccionario_acciones = {
                                "C": contar_palabras,
                                "R": remplazar_palabras,
                                "E": eliminar_palabra
    }
    return diccionario_acciones[accion]()    

try:
    texto = "La casas de Mateo es muy grande tiene incluso una pista de tenis en su jardin"
    accion = input("¿Que quieres hacer?: Contar (C), Reemplazar (R), Eliminar (E) palabras: ")[0].upper().strip()
    print(procesar_texto(texto, accion))
except KeyError:
    print("ERROR: Debe elegir una accion valida.")
except ValueError:
    print("No existe esa palabra dentro del texto" )