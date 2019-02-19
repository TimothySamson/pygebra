import expr

def deriv(self, wrt): 
    if expr.isConst(self):
        return 0
    
    if expr.isTree(self):
        left = self.node1
        right = self.node2
        if self.oper == "+":
            return deriv(left, wrt) + deriv(right, wrt)

        if self.oper == "*":
            return deriv(left, wrt)*right + deriv(right, wrt)*left
        
        if self.oper == "^":
            if expr.isConst(right):
                return right * left ** (right - 1) * deriv(left, wrt)

    return self.deriv(wrt)
        




