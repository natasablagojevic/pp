# trocifren ABC?
# A,B, C razliciti brojevi 
# min ABC/(A+B+C) 

import constraint 

problem = constraint.Problem()

problem.addVariable('A', range(1, 10))
problem.addVariables('BC', range(10))

problem.addConstraint(constraint.AllDifferentConstraint())




solutions = problem.getSolutions()

best_solution = solutions[0]

def evaluate(solution):
    # alternativa;
    # set(solutions.keys()) == set('A', 'B', 'C')
    assert isinstance(solution, dict) and \
        'A' in solution and 'B' in solution and \
            'C' in solution, 'Fatal error: invalid argument'
    
    A = solution['A']
    B = solution['B']
    C = solution['C']
    
    return (100*A + 10*B + C)/(A + B + C)

for solution in solutions[1:]:
    if (evaluate(solution) < evaluate(best_solution)):
        best_solution = solution 
        
print(best_solution, evaluate(best_solution))
print(type(best_solution))