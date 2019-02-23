from expr import *

x = Var("x")
y = Var("y")
z = Var("z")

print(deriv(3 * y , y))
print(isConst(ExprTree(5, "*", 6)))
print(deriv(ln(sin(cos(x * y))), y))
print(6 / (x * y) ** 2)
print((x**2) ** -3)
print((x * y) / z)
print(abs((x*y) ** z))
print(ln(e * pi))
print(deriv(2 ** x, x))

t = Var("t")
expr = 2*cos(t) - 3*sin(t)
print(deriv(deriv(expr, t), t) + expr)

expr1 =1/x + y * x
expr2 = 2*y*x**2 - cos(y)

print(deriv(expr1, y))
print(deriv(expr2, x))

expr1 = e**x * y + x*e**x * y
expr2 = x*e**x + 2

print(deriv(expr1, y))
print(deriv(expr2, x))

print(deriv(x**2 / x, x))

print((evaluate(e**(x*y*z), y,  2)))

print(deriv((e**y)**x, x))

print(expand((x+1) * (x+1) * (x+1)))
print(expand((x+1)**ln(2*e)))
