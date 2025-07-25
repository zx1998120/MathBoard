from fastapi import APIRouter
from models.schemas import OptimizeRequest
from platypus import Problem, Real, NSGAII, nondominated

router = APIRouter()

@router.post("/")
def optimize(req: OptimizeRequest):
    def objectives(x):
        f1 = x[0]
        g = 1 + 9 * sum(x[1:]) / (req.num_variables - 1)
        f2 = g * (1 - (f1 / g)**0.5)
        return [f1, f2]

    problem = Problem(req.num_variables, 2)
    problem.types[:] = [Real(lb, ub) for lb, ub in zip(req.lower_bounds, req.upper_bounds)]
    problem.function = objectives

    algorithm = NSGAII(problem, population_size=req.population_size)
    algorithm.run(req.generations)

    front = [[s.objectives[0], s.objectives[1]] for s in nondominated(algorithm.result)]
    return {"pareto_front": front}