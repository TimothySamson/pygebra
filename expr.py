from numbers import Number
from fractions import Fraction
from operations import operationMixin

# MAIN THINGS I WANT TO DO
# 0.) Evaluate
# 2.) Expand
# 3.) Solve for x
# 4.) Test for equality (gotta be dirty here mehn)

class Object(operationMixin):
    # ----- Machinery ----
    def __add__(self, node2):
        return Object.add(self, node2)

    def __mul__(self, node2):
        return Object.mul(self, node2)

    def __pow__(self, node2):
        return Object.pow(self, node2)

    # ----- Convenience ----

    def __sub__(self, node2):
        return self + -1*node2

    def __truediv__(self, node2):
        return self * node2**(-1)
    
    # ----- Right methods -----
    # Here the other argument is on the left.

    def __radd__(self, node2):
        return Object.add(node2, self)

    def __rmul__(self, node2):
        return Object.mul(node2, self)

    def __rpow__(self, node2):
        return Object.pow(node2, self)

    # ----- Right Convenience ----

    def __rsub__(self, node2):
        return Object.add(node2, -self)
    
    def __rtruediv__(self, node2):
        return Object.mul(node2, self ** (-1))

    # ----- Unary ---

    def __neg__(self):
        return -1 * self

    def __abs__(self):
        return absolute(self)


    
    # ----- TEMPLATE ----

class Leaf(Object):
    def __str__(self):
        raise NotImplementedError

    def deriv(self, wrt):
        raise NotImplementedError

class Var(Leaf):
    def __init__(self, varName):
        self.name = varName

    def __eq__(self, other):
        return isinstance(other, Var) and other.name == self.name

    def deriv(self, wrt):
        if self == wrt:
            return 1
        else:
            return 0

    def __str__(self):
        return self.name

class ExprTree(Object):
    def __init__(self, node1, oper, node2):
        self.node1 = node1
        self.oper = oper
        self.node2 = node2

    def __str__(self):
        if self.oper == "*":
            if self.node1 == -1:
                return f"-{self.node2}"
            if self.node2 == -1:
                return f"-{self.node1}"
            
            try: 
                if self.node2.node2 < 0 and self.node2.oper == "^":
                    return f"({self.node1} / ({self.node2.node1 ** abs(self.node2.node2)}))"
            except (AttributeError, TypeError):
                pass

            try: 
                if self.node1.node2 < 0 and self.node1.oper == "^":
                    return f"({self.node2} / ({self.node1.node1 ** -(self.node1.node2)}))"
            except (AttributeError, TypeError):
                pass
        
        if self.oper == "^":
            if isConst(self.node2):
                if self.node2 < 0:
                    return f"(1 / {self.node1 ** -(self.node2)})"

        return f"({self.node1} {self.oper} {self.node2})"


def isConst(tree):
    if isTree(tree):
        return isConst(tree.node1) and isConst(tree.node2)
    return isinstance(tree, Number) or isinstance(tree, Const)

def isTree(tree):
    return isinstance(tree, ExprTree)

def isInt(const):
    pass

def refresh(tree, func=(lambda a: a)):
    if tree.oper == "+":
        return func(tree.node1) + func(tree.node2)
    if tree.oper == "*":
        return func(tree.node1) * func(tree.node2)
    if tree.oper == "^":
        return func(tree.node1) ** func(tree.node2)

from eq.eq import eq 
from simplify.simplify import simplify
from simplify.eval import *
from constants import *
from derivative.derivative import deriv
from functions.functions import *
