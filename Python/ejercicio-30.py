# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def comprobar_anagramas(x, y):
    anagrama = sorted(x.lower().strip()) == sorted(y.lower().strip())
    print("Son anagrama" if anagrama else "No son anagrama")

comprobar_anagramas("Sergio", "Riesgo ")
comprobar_anagramas("Callejon", "Vallejo")