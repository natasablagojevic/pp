# moze da dodje na ispitu
# Kiflica: hleb, kifle          [20h]
# hleb: 10min, kifla: 12min     [10kg]
# hleb: 300gr, kifla: 120gr
# hleb: 7din, kifla: 9din

import constraint 

problem = constraint.Problem()

# broj helbova  : 10*1000/300
problem.addVariable('hleb', range(int(min(20*60/10, 10*1000/300)) + 1))

# broj kifli:
problem.addVariable('kifla', range(int(min(20*60/12, 10*1000/120)) + 1))

def ogr_vreme(hleb, kifla):
    return 10*hleb + 12*kifla <= 20*60
    
def ogr_velicina(hleb, kifla):
    return 300*hleb + 120*kifla <= 10*1000

problem.addConstraint(ogr_vreme, ['hleb', 'kifla'])
problem.addConstraint(ogr_velicina, ['hleb', 'kifla'])

solutions = problem.getSolutions()
max = solutions[0]

for solution in solutions:
    if (7*solution['hleb'] + 9*solution['kifla']) > 7*max['hleb'] + 9*max['kifla']:
        max = solution
        
print(max)
print(7*max['hleb'] + 9*max['kifla'])