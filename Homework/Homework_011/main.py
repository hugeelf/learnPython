# Дана функция f(x) = 18x^3+5x^2 + 10x - 30
import sympy
our_func = sympy.sympify("18*x**3+5*x**2 + 10*x - 30")
x = sympy.Symbol('x')

# Построить график
sympy.plotting.plot(our_func)

# Определить корни
a = sympy.solve(our_func,x)
print(a)

# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
print(sympy.solve(our_func > 0,x))
print(sympy.solve(our_func < 0,x))


# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0
diff =  sympy.diff(our_func,x)
print(diff)
print(sympy.solve(diff > 0,x))
print(sympy.solve(diff < 0,x))

# 5. Вычислить вершину
print(sympy.solve(diff,x))