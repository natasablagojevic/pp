import constraint 

problem = constraint.Problem()

problem.addVariable('duzina', range(4))
problem.addVariable('sirina', range(4))
problem.addVariable('visina', range(10))

# def ogranicenje(d, s, v):
#     if d != s and d != v and s != v:
#         return True
    
# problem.addConstraint(ogranicenje, ['duzina', 'sirina', 'visina'])
# problem.addConstraint(constraint.AllDifferentConstraint())
problem.addConstraint(constraint.AllEqualConstraint())

solutions = problem.getSolutions()

for solution in solutions:
    print(solution)
    
# default constraints:
#   1. constraint.MaxSumConstraint()    : maksimizacija sume
#   2. constraint.MinSumConstraint()    : 
#   3. constraint.ExactSumConstraint()  :
#   4. constraint.InSetConstraint()     :
#   5. ...