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
