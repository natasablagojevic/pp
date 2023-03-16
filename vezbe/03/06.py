# Magican kvadrat

# A B C
# D E F
# G H I 

import constraint 

problem = constraint.Problem()

problem.addVariables('ABCDEFGHI', range(1, 10))

problem.addConstraint(constraint.AllDifferentConstraint())
def ogr(x, y, z):
    return x + y + z == 15

problem.addConstraint(ogr, 'ABC')
problem.addConstraint(ogr, 'DEF')
problem.addConstraint(ogr, 'GHI')
problem.addConstraint(ogr, 'ADG')
problem.addConstraint(ogr, 'BEH')
problem.addConstraint(ogr, 'CFI')
problem.addConstraint(ogr, 'AEI')
problem.addConstraint(ogr, 'CEG')


solutions = problem.getSolutions()

for solution in solutions:
    print(f"{solution['A']} {solution['B']} {solution['C']}")
    print(f"{solution['D']} {solution['E']} {solution['F']}")
    print(f"{solution['G']} {solution['H']} {solution['I']}")
    print('-----')