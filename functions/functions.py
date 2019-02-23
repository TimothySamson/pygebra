import expr
import math

class Function(expr.Leaf):
    def __init__(self, arg):
        self.arg = arg

    def evaluate(self):
        raise NotImplementedError
    
    def numeric(self):
        if expr.isConst(self.arg):
            self.arg = expr.numeric(self.arg)
            return self.evaluate()
        else:
            self.arg = expr.numeric(self.arg)
            return self

class sinClass(Function):
    def deriv(self, wrt):
        return cos(self.arg) 

    def __str__(self):
        return f"sin({self.arg})"

    def evaluate(self):
        return math.sin(self.arg)

class cosClass(Function):
    def deriv(self, wrt):
        return -sin(self.arg)

    def __str__(self):
        return f"cos({self.arg})"

    def evaluate(self):
        return math.cos(self.arg)

class absoluteClass(Function):
    def deriv(self, wrt):
        return absolute(self.arg) / self.arg

    def __str__(self):
        return f"|{self.arg}|"

    def evaluate(self):
        return abs(self.arg)

class lnClass(Function):
    def deriv(self, wrt):
        return 1 / self.arg

    def __str__(self):
        return f"ln({self.arg})"

    def evaluate(self):
        return math.log(self.arg)

def ln(arg):
    if arg == expr.e:
        return 1
    return lnClass(arg)

def cos(arg):
    return cosClass(arg)

def sin(arg):
    return sinClass(arg)

def absolute(arg):
    return absoluteClass(arg)
