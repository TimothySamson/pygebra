import expr

class operationMixin:
    @staticmethod
    def add(left, right):
        if left == 0:
            return right
        if right == 0:
            return left

        return expr.ExprTree(left, "+", right)

    @staticmethod
    def mul(left, right):
        if left == 0:
            return 0
        if right == 0:
            return 0

        if left == 1:
            return right
        if right == 1:
            return left

        return expr.ExprTree(left, "*", right)

    @staticmethod
    def pow(base, exp):
        if exp == 0:
            return 1
        if base == 0:
            return 0
        if exp == 1:
            return base
        if base == 1:
            return 1
        
        if expr.isTree(base):
            if base.oper == "^":
                return expr.ExprTree(base.node1, "^", (base.node2 * exp))

        return expr.ExprTree(base, "^", exp)
