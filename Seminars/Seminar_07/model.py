# нахождение решения, передача в logger и ui
import sympy

def solution (expr):
    x = sympy.Symbol('x')
    return str(sympy.solve(expr,x))

