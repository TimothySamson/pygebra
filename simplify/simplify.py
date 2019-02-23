import expr

# factor * (addtree.node1 + addtree.node2)
def leftFoil(factor, addTree):
    return factor * addtree.node1 + factor * addTree.node2


def simplify(exprTree):
    if not expr.isTree(exprTree):
        return exprTree

    left = exprTree.node1
    right = exprTree.node2

    if exprTree.oper == "+":
        return simplify(left) + simplify(right)

    if exprTree.oper == "*":
        if left.oper == "+":
            return simplify(leftFoil(right, left))
        if right.oper == "+":
            return simplify(leftFoil(left, right))

    if exprTree.oper == "^":
        if isConst(right):
            pass
