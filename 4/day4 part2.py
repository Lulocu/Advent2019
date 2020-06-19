dRange = 124075
uRange = 580769
res = 0
for number in range(dRange,uRange+1):
    numero = list(map(int,str(number)))
    pred = -1
    Dec = True
    Doble = False
    dicRep = {}
    for elemento in numero:
        if elemento < pred:
            Dec = False
            break
        if elemento == pred:
            dicRep[elemento] = dicRep.get(elemento,1) + 1

        pred = elemento

    if Dec:
        for llave in dicRep.keys():
            if dicRep[llave] == 2:
                res+=1
                break

print(res)