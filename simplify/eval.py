import expr

# Var could either be a list or a single object
def evaluate(obj, var, repl):
    if expr.isTree(obj):
        return expr.refresh(obj, lambda x: evaluate(x, var, repl))
    
    try:
        if obj in var:
            return repl[var.index(obj)]
        else:
            return obj
    except TypeError: 
        if obj == var:
            return repl
        else:
            return obj

def numeric(obj):
    if not expr.isTree(obj):
        try:
            return obj.numeric()
        except (AttributeError, NotImplementedError):
            return obj

    return expr.refresh(obj, numeric)
