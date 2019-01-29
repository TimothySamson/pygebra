from enum import Enum

class Object:
    @staticmethod
    def add(node1, node2):
        if node1 == 0:
            return node2
        if node2 == 0:
            return node1

        return ExprTree(node1, "+", node2)

    @staticmethod
    def mul(node1, node2):
        if node1 == 0 or node2 == 0:
            return 0

        if node1 == 1:
            return node2
        if node2 == 1:
            return node1

        return ExprTree(node1, "*", node2)

    @staticmethod
    def pow(node1, node2):
        if node2 == 0:
            return 1
        if node1 == 0:
            return 0
        if node1 == 1:
            return 1
        if node2 == 1:
            return node1

        return ExprTree(node1, "^", node2)

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

    # TODO: Make it so that it respects the order

    def __radd__(self, node2):
        return Object.add(node2, self)

    def __rmul__(self, node2):
        return Object.mul(node2, self)

    def __rpow__(self, node2):
        return ExprTree(node2, "^", self)

    # ----- Right Convenience ----

    def __rsub__(self, node2):
        return Object.add(node2, -self)
    
    def __rtruediv__(self, node2):
        return Object.mul(node2, self ** (-1))

    # ----- Unary ---

    def __neg__(self):
        return -1 * self

class Leaf(Object):
    def __str__(self):
        return str(self.name)

class Var(Leaf):
    def __init__(self, varName):
        self.name = varName

    def eval(self, varName, num):
        if varName == self.varName:
            return num
        else:
            return self

class ExprTree(Object):
    def __init__(self, node1, oper, node2):
        self.node1 = node1
        self.oper = oper
        self.node2 = node2

    def __str__(self):
        return f"({self.node1} {self.oper} {self.node2})"


print(5 * Var("x") * Var("y") / Var("z"))
