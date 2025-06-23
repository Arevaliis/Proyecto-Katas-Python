# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    contador = {}
    for num in lista:
        if  num not in contador.keys():
            contador[num] = 1
        else: 
            contador[num] += 1 

        if contador[num] == 2:
            return f"El primer elemento duplicado es {num}"
        
valor_duplicado = primer_duplicado([0,1,7,8,2,3,3,4,5,2,3])
print(valor_duplicado)