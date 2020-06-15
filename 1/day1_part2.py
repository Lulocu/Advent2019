import math  as math

"""
Day 1 of advent of code
param: None
return: integer with total
"""
def fuel(mass):

    parcial = mass / 3
    parcial = math.trunc(parcial) - 2

    if parcial <= 0:
        return 0
        
    return parcial + fuel(parcial)


parcial = 0
total = 0
fh = open('input.txt',"r")
for line in fh:
    gasolina = int(line)
    total = total + fuel(gasolina)

print(total)
