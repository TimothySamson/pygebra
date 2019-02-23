import expr

def evaluate(tree, var, obj):
    if expr.isTree(tree):
        return expr.refresh(tree, lambda x: evaluate(x, var, obj))

    if tree == var:
        return obj
    else:
        return tree

def numeric(tree):
    if not expr.isTree(tree):
        try:
            return tree.numeric()
        except (AttributeError, NotImplementedError):
            return tree

    return expr.refresh(tree, numeric)

        
