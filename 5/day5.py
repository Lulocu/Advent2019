"""
Advent of code 2019 day 5
"""  
#mapeos
parar = 99
sumar = 1
multiplicar = 2
entrada = 3
salida = 4
saltarSiTrue = 5
saltarSiFalse = 6
menor = 7
igual = 8




def calcular1Param(nCeldilla,codigoParametros):
    codigoParametros = list(map(int, str(codigoParametros)))
    if len(codigoParametros) < 1:
        return cinta[cinta[nCeldilla + 1]]
    else:
        return cinta[nCeldilla+1]

def calcular2Param(nCeldilla,codigoParametros):
    codigoParametros = list(map(int, str(codigoParametros)))
    if len(codigoParametros) < 2:
        codigoParametros.insert(0,0)

    if codigoParametros[-1] == 0:
        operando = cinta[cinta[nCeldilla + 1]]
    else:
        operando = cinta[nCeldilla+1]

    if codigoParametros[-2] == 0:
        destino = cinta[cinta[nCeldilla + 2]]
    else:
        destino = cinta[nCeldilla + 2]

    return[operando,destino]

def calcular3Param(nCeldilla,codigoParametros):
    codigoParametros = list(map(int, str(codigoParametros)))
    while len(codigoParametros) < 2:
        codigoParametros.insert(0,0)
    if codigoParametros[-1] != 1:
        operando1 = cinta[cinta[nCeldilla + 1]]
    else:
        operando1 = cinta[nCeldilla+1]

    if codigoParametros[-2] != 1:
        operando2 = cinta[cinta[nCeldilla + 2]]
    else:
        operando2 = cinta[nCeldilla + 2]

    destino =  cinta[nCeldilla + 3]
    return[operando1,operando2,destino]


fh = open("input.txt",'r')

cinta = fh.read()
cinta = cinta.rsplit(',')
cinta = list(map(int,cinta))

nCeldilla = 0
while nCeldilla < len(cinta):
    aux=str(cinta[nCeldilla])
    codigoOperacion = int(aux[-2:])
    codigoParametros = aux[0:-2]

    if codigoOperacion == parar:
        break

    elif codigoOperacion == sumar:
        [sumando1, sumando2, destino] = calcular3Param(nCeldilla,codigoParametros)
        cinta[destino]  = sumando1 + sumando2
        nCeldilla += 4

    elif codigoOperacion == multiplicar:
        [multiplicando1, multiplicando2,destino] = calcular3Param(nCeldilla,codigoParametros)
        cinta[destino]  = multiplicando1 * multiplicando2
        nCeldilla += 4

    elif codigoOperacion == entrada:
        print("Escriba el input del programa:")
        inputNumber = input()
        cinta[cinta[nCeldilla+1]] = int(inputNumber)
        nCeldilla += 2

    elif codigoOperacion == salida:
        destino = calcular1Param(nCeldilla,codigoParametros)
        print(destino)
        nCeldilla += 2

    elif codigoOperacion == saltarSiTrue:
        [operando,destino] = calcular2Param(nCeldilla,codigoParametros)
        if operando != 0:
            nCeldilla = destino
        else:
            nCeldilla += 3

    elif codigoOperacion == saltarSiFalse:
        [operando,destino] = calcular2Param(nCeldilla,codigoParametros)
        if operando == 0:
            nCeldilla = destino
        else:
            nCeldilla += 3

    elif codigoOperacion == menor:
        [operando1,operando2,destino] = calcular3Param(nCeldilla,codigoParametros)
        if operando1 < operando2:
            cinta[destino] = 1
        else:
            cinta[destino] = 0
        nCeldilla += 4

    elif codigoOperacion == igual:
        [operando1,operando2,destino] = calcular3Param(nCeldilla,codigoParametros)
        if operando1 == operando2:
            cinta[destino] = 1
        else:
            cinta[destino] = 0
        nCeldilla += 4

    else:
        raise Exception('Code op at nCeldillaition %f is not correct. Code = %f',nCeldilla,cinta[nCeldilla])

