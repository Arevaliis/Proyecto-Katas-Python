# 22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

from functools import reduce

producto_total = reduce(lambda x, y: x * y, [1,2,4,10])
print(producto_total)