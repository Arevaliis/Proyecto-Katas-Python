""" 
34. Crea la clase Arbol
- Define un árbol genérico con un tronco y ramas como atributos.
- Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.

Código a seguir:
- Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
- Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
-   Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
-   Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
-   Implementar el método quitar_rama para eliminar una rama en una posición específica.
-   Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.

Caso de uso:

1. Crear un árbol.
2. Hacer crecer el tronco una unidad.
3. Añadir una nueva rama.
4. Hacer crecer todas las ramas una unidad.
5. Añadir dos nuevas ramas.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol.
"""

class Arbol():

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        if self.ramas:
            self.ramas = [rama + 1 for rama in self.ramas]
        else:
            print("No pueden crecer las ramas porque este arbol no tiene ramas todavia")

    def quitar_rama(self, posicion):
        if posicion in range(1, len(self.ramas) + 1):
            self.ramas.pop(posicion - 1)
            print(f"Rama eliminada en la posicion {posicion}")
        else: 
            print(f"No hay ninguna rama en la posicion {posicion}")

    def info_arbol(self):
        print(f"""
            La longitud del tronco es de {self.tronco} metros.
            Tiene un total de {len(self.ramas)} ramas.
            Longitud de las ramas {", ".join([str(rama)for rama in self.ramas])}.
                """)

nuevo_arbol = Arbol()
nuevo_arbol.crecer_tronco()
nuevo_arbol.crecer_ramas()
nuevo_arbol.nueva_rama()
nuevo_arbol.info_arbol()

nuevo_arbol.crecer_ramas()
nuevo_arbol.info_arbol()

nuevo_arbol.nueva_rama()
nuevo_arbol.nueva_rama()
nuevo_arbol.info_arbol()

nuevo_arbol.quitar_rama(posicion=90)
nuevo_arbol.quitar_rama(posicion=3)
nuevo_arbol.info_arbol()