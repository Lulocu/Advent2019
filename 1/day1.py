import math  as math

"""
Day 1 of advent of code
param: None
return: integer with total
"""
parcial = 0
total = 0
fh = open('input.txt',"r")
for line in fh:
    parcial = int(line) / 3
    parcial = math.trunc(parcial) - 2
    total = total + parcial
print(total)
