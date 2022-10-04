# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
import my_lib
d = str(input('введите D: '))
print(round(math.pi, len(my_lib.slicer(d))))
