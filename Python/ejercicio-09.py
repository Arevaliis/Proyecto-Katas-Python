""" 
9. Escribe una función que tome una lista de nombres de mascotas como parámetro
y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. 
Usa la función filter().
"""

def animales_prohibidos(animal):
    return animal not in ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

animales_permitidos = list(filter(animales_prohibidos, ["Perro",  "Hamster", "Gato", "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", "Conejo", "Cabra"]))
print(animales_permitidos)