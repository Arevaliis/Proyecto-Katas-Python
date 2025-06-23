# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

diferencia = reduce(lambda x,y: x - y, [2,4,7,12,5,20])
print(diferencia)