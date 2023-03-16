# novcici
# 1, 2, 5, 10, 20
# kako do 50 dinara?

import constraint 
import time 

problem = constraint.Problem()

# koliko imam koje novcanice? broj
problem.addVariable('1din', range(51))
problem.addVariable('2din', range(26))
problem.addVariable('5din', range(11))
problem.addVariable('10din', range(6))
problem.addVariable('20din', range(3))

def ogranicenje(kd1, kd2, kd5, kd10, kd20):
    if (kd1 + 2*kd2 + 5*kd5 + 10*kd10 + 20*kd20) == 50:
        return True 
    
# problem.addConstraint(ogranicenje, ['1din', '2din', '5din', '10din', '20din'])

problem.addConstraint(constraint.ExactSumConstraint(50, [1, 2, 5, 10, 20]), ['1din', '2din', '5din', '10din', '20din'])

start_t = time.time()
solutions = problem.getSolutions()
end_t = time.time()

for solution in solutions:
    print(solution)
    
print(f'In {end_t - start_t}')