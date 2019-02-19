from expr import *

x = Var("x")
y = Var("y")
z = Var("z")

print(deriv(3 * y , y))
print(isConst(ExprTree(5, "*", 6)))


