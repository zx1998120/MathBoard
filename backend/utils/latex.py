from sympy.printing.latex import latex

def to_latex(expr):
    return f"$$ {latex(expr)} $$"