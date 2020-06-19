"""
Advent of code 2019 day 2
"""  
#mapeos
parar = 99
sumar = 1
multiplicar = 2

fh = open("input.txt",'r')

cinta = fh.read()
cinta = cinta.rsplit(',')

cinta[1] = 12
cinta[2] = 2
cinta = list(map(int,cinta))

for op in range(0,len(cinta),4):

    if cinta[op] == parar:
        break

    elif cinta[op] == sumar:
        cinta[cinta[op+3]]  = cinta[cinta[op+1]] + cinta[cinta[op+2]]

    elif cinta[op] == multiplicar:
        cinta[cinta[op+3]]  = cinta[cinta[op+1]] * cinta[cinta[op+2]]

    else:
        raise Exception('Code op at position %f is not correct. CodeOp = %f',op,cinta[op])

print(cinta[0])
