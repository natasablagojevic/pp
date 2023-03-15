# biblioteka za ogranicenja
import constraint

# 1. definisanje problema
problem = constraint.Problem()
# print(problem)

# 2. definisanje promenljivih
problem.addVariable('x', ['a', 'b', 'c'])
problem.addVariable('y', [1, 2])
problem.addVariable('z', [0.1, 0.2, 0.3])

# 3. definisanje ogranicenja i dodavanje ogranicenja
# ako je ogranicenje zadovoljeno vracamo True
# a ako nije Fale, ne mora eksplicitno da se navodi
def condition(y, z):
    if y/10 == z:
        return True
    else:
        return False

#                       f-ja        njeni parametri
problem.addConstraint(condition, ['y', 'z'])

# 4. resavanje
# vraca listu resenja koji su recnici
# keys - tipovi promenljive
# values - resenja, njena vrednost
resenja = problem.getSolutions()

for r in resenja:
    print(r)

# print(resenja)
