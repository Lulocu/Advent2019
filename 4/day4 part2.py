from collections import Counter
dRange = 124075
uRange = 580769
res = 0
numRep = []
for number in range(dRange,uRange+1):
    numero = list(map(int,str(number)))
    pred = -1
    Rep = False
    Dec = True
    for elemento in numero:
        if elemento < pred:
            Dec = False
            break
        if elemento == pred:
            Rep = True
            numRep = numRep + [elemento]
        pred = elemento

    if Dec and Rep:
        c = Counter(numRep)
        anadir = False
        for llave in c.keys():
            if c[llave] == 1:
                anadir = True
                break
        if anadir:
            res+=1

print(res)