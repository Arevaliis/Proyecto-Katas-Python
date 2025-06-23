""" 
5. Escribe una función que tome una lista de números como parámetro y un valor opcional
nota_aprobado (por defecto 5). La función debe calcular la media de los números en la 
lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado 
será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que 
contenga la media y el estado.
"""

def nota_final(notas, nota_min_aprobar = 5):
    nota_media =  round(sum(notas) / len(notas), 2)
    if nota_media >= nota_min_aprobar:
        return "Has Aprobado", nota_media
    else:
        return "Suspenso", nota_media
    
tupla = nota_final([5.34,6.5,4.2])
print(tupla)