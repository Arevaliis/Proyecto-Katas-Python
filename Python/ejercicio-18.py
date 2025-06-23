# 18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

estudiantes = [
    {"nombre": "Juan", "edad": 20, "calificación": 85},
    {"nombre": "María", "edad": 22, "calificación": 90},
    {"nombre": "Carlos", "edad": 21, "calificación": 78},
    {"nombre": "Ana", "edad": 23, "calificación": 95},
    {"nombre": "Luis", "edad": 20, "calificación": 88},
]

alumnos_sobresalinetes = list(filter(lambda x: x['calificación'] >= 90, estudiantes))
print(alumnos_sobresalinetes)