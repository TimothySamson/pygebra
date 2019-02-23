import expr
from constants import *
from functions.functions import *

def deriv(self, wrt): 
    if expr.isConstWrt(self, wrt):
        return 0
    
    if expr.isTree(self):
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
    left = self.node1
    right = self.node2
    return deriv(left, wrt) + deriv(right, wrt)

def mul(self, wrt):
    left = self.node1
    right = self.node2
    return deriv(left, wrt)*right + deriv(right, wrt)*left

def pow(self, wrt):
    left = self.node1
    right = self.node2

    if expr.isConstWrt(right, wrt):
        return right * left ** (right - 1) * deriv(left, wrt)
    
    if expr.isConstWrt(left, wrt):
        return ln(left) * left ** right * deriv(right, wrt)


