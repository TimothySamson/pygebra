import expr

def deriv(self, wrt): 
    if expr.isConst(self):
        return 0
    
    if expr.isTree(self):
        left = self.node1
        right = self.node2
        if self.oper == "+":
            return add(self, wrt)

        if self.oper == "*":
            return mul(self, wrt)
        
        if self.oper == "^":
            return pow(self, wrt)
    
    try:
        # When it's a function
        return self.deriv(wrt) * deriv(self.arg, wrt)
    except AttributeError:
        # When it's a variable
        return self.deriv(wrt)

def add(self, wrt):
    return deriv(left, wrt) + deriv(right, wrt)

def mul(self, wrt):
    left = self.node1
    right = self.node2
    return deriv(left, wrt)*right + deriv(right, wrt)*left

def pow(self, wrt):
    left = self.node1
    right = self.node2

    if expr.isConst(right):
        return right * left ** (right - 1) * deriv(left, wrt)

    if expr.isConst(left):
        return 


