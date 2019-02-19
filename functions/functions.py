import expr

class Function(expr.Leaf):
    def __init__(self, arg):
        raise NotImplementedError
    def eval(self, num):
        raise NotImplementedError


class sin(Function):
    def __init__(self, arg):
        self.arg = arg

    def deriv(self, wrt):
        return cos(self.arg) 

    def __str__(self):
        return f"sin({self.arg})"

class cos(Function):
    def __init__(self, arg):
        self.arg = arg
    
    def deriv(self, wrt):
        return -sin(self.arg)

    def __str__(self):
        return f"cos({self.arg})"

class absolute(Function):
    def __init__(self, arg):
        self.arg = arg
    
    def deriv(self, wrt):
        return absolute(self.arg) / self.arg

    def __str__(self):
        return f"|{self.arg}|"

class ln(Function):
    def __init__(self, arg):
        self.arg = arg

    def deriv(self, wrt):
        return 1 / self.arg

    def __str__(self):
        return f"ln({self.arg})"


