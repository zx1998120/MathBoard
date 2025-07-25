from fastapi import APIRouter
from models.schemas import SymbolicRequest
from sympy import symbols, simplify, diff, integrate, series, sympify
from utils.latex import to_latex

router = APIRouter()

@router.post("/")
def process_symbolic(req: SymbolicRequest):
    x = symbols(req.variable)
    expr = sympify(req.expression)

    if req.operation == 'simplify':
        result = simplify(expr)
        steps = [to_latex(expr), to_latex(result)]
    elif req.operation == 'diff':
        result = diff(expr, x)
        steps = [to_latex(expr), to_latex(result)]
    elif req.operation == 'integrate':
        result = integrate(expr, x)
        steps = [to_latex(expr), to_latex(result)]
    elif req.operation == 'taylor':
        result = series(expr, x, n=req.order).removeO()
        steps = [to_latex(expr), to_latex(result)]
    else:
        return {"error": "Invalid operation"}

    return {"steps": steps, "result": to_latex(result)}