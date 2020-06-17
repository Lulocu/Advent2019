dRange = 124075
uRange = 580769
res = 0
for number in range(dRange,uRange):
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
        pred = elemento

    if Dec and Rep:
        res+=1

print(res)