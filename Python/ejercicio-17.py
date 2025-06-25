# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

from functools import reduce

numero_concatenado = int(reduce( lambda x, y: str(x) + str(y), [5,7,2,3,4]))
print(numero_concatenado)