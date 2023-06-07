import constraint 

problem = constraint.Problem()

problem.addVariable('B', range(10))
problem.addVariable('C', range(20))
problem.addVariable('D', range(7))
problem.addVariable('M', range(5))  # magnezijum
problem.addVariable('S', range(3))  # selen
problem.addVariable('Z', range(9))  # cink

# ogranicenje ukupne cene
problem.addConstraint(lambda b, c, d, m, s, z: 130*b + 800*c + 150*d + m*370 + s*490 + 150*z <= 100*118, "BCDMSZ")


# ogranicenje sinteze proteina 
problem.addConstraint(lambda b, c, d, m, s, z: 15*b + 11*c+10*d+22*m+1*s+13*z <= 100, "BCDMSZ")

# ogranicenje sinteze amino-kiseline 
problem.addConstraint(lambda b,c,d,m,s,z: 33*b+31*c+20*d+18*m+21*s+16*z <= 200, "BCDMSZ")

# ogranicenje sinteze hemoglobina:
problem.addConstraint(lambda b,c,d,m,s,z: b*92.5+c*155.5+d*79.6+m*156.2+s*413+z*137.7, "BCDMSZ")

max_hemaglobin = 0 
max_mapa = {}

def evaluate_hemoglobin(b,c,d,m,s,z):
    return 92.5*b + 155.5*c + 79.6*d + 156.2*m + 413*s + 137.7*z 

results = problem.getSolutions()

if results:
    for r in results:
        hem = evaluate_hemoglobin(r['B'], r['C'], r['D'], r['M'], r['S'], r['Z'])
        
        if hem > max_hemaglobin:
            max_hemaglobin = hem 
            max_mapa = r 
            
    print(round(hem, 2))
else:
    print("Nije moguce sitetisati hemoglobin")