import expr
import math

class Const(expr.Leaf):
    def numeric(self):
        return NotImplementedError

class pi(Const):
    def __str__(self):
        return "pi"

    def numeric(self):
        return math.pi

class e(Const):
    def __str__(self):
        return "e"

    def numeric(self):
        return math.e

e = e()
pi = pi()

