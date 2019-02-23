import expr

# factor * (addtree.node1 + addtree.node2)
def leftFoil(factor, addTree):
    return factor * addTree.node1 + factor * addTree.node2


def expand(exprTree):
    if not expr.isTree(exprTree):
        return exprTree

    left = expand(exprTree.node1)
    right = expand(exprTree.node2)

    if exprTree.oper == "+":
        return expand(left) + expand(right)

    if exprTree.oper == "*":
        if expr.isTree(left):
            if left.oper == "+":
                return expand(leftFoil(right, left))

        if expr.isTree(right):
            if right.oper == "+":
                return expand(leftFoil(left, right))

    if exprTree.oper == "^":
        if expr.isInt(right):
            right = int(expr.numeric(right))
            return expand(left * left ** (right - 1))

    return exprTree

