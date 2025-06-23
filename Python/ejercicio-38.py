""" 
38. Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
Reglas:

    -  0 - 69: insuficiente
    -  70 - 79: bien
    -  80 - 89: muy bien
    -  90 - 100: excelente
"""

def calificacion(nota):
    print("Excelente" if nota >= 90 else ("Muy Bien" if nota >= 80 else ("Bien" if nota >= 70 else "Insuficiente")))

calificacion(60)
calificacion(69)
calificacion(70)
calificacion(80)
calificacion(100)