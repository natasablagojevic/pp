# sortiranje
import math

tacke = [(1, 2), (32, 2), (-1, -1), (0, 2)]

def l2(t):
    return math.sqrt((t[0]**2 + t[1]**2)**2)


print(tacke)
print(sorted(tacke, reverse=True))
print(sorted(tacke, key=l2))
print(sorted(tacke, key=lambda t: (t[0]**2 + t[1]**2)**2))
