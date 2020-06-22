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




def calcular1Param(pos,paramCode):
    paramCode = list(map(int, str(paramCode)))
    if len(paramCode) < 1:
        return cinta[cinta[pos + 1]]
    else:
        return cinta[pos+1]

def calcular2Param(pos,paramCode):
    paramCode = list(map(int, str(paramCode)))
    if len(paramCode) < 2:
        paramCode.insert(0,0)

    if paramCode[-1] == 0:
        variable = cinta[cinta[pos + 1]]
    else:
        variable = cinta[pos+1]

    if paramCode[-2] == 0:
        destino = cinta[cinta[pos + 2]]
    else:
        destino = cinta[pos + 2]

    return[variable,destino]

def calcular3Param(pos,paramCode):
    paramCode = list(map(int, str(paramCode)))
    while len(paramCode) < 2:
        paramCode.insert(0,0)
    if paramCode[-1] != 1:
        operando1 = cinta[cinta[pos + 1]]
    else:
        operando1 = cinta[pos+1]

    if paramCode[-2] != 1:
        operando2 = cinta[cinta[pos + 2]]
    else:
        operando2 = cinta[pos + 2]

    destino =  cinta[pos + 3]
    return[operando1,operando2,destino]


fh = open("input.txt",'r')

cinta = fh.read()
cinta = cinta.rsplit(',')
cinta = list(map(int,cinta))

pos = 0
while pos < len(cinta):
    aux=str(cinta[pos])
    codeOp = int(aux[-2:])
    paramCode = aux[0:-2]

    if codeOp == parar:
        break

    elif codeOp == sumar:
        [sumando1, sumando2, destino] = calcular3Param(pos,paramCode)
        cinta[destino]  = sumando1 + sumando2
        pos += 4

    elif codeOp == multiplicar:
        [multiplicando1, multiplicando2,destino] = calcular3Param(pos,paramCode)
        cinta[destino]  = multiplicando1 * multiplicando2
        pos += 4

    elif codeOp == entrada:
        print("Escriba el input del programa:")
        inputNumber = input()
        cinta[cinta[pos+1]] = int(inputNumber)
        pos += 2

    elif codeOp == salida:
        destino = calcular1Param(pos,paramCode)
        print(destino)
        pos += 2

    elif codeOp == saltarSiTrue:
        [variable,destino] = calcular2Param(pos,paramCode)
        if variable != 0:
            pos = destino
        else:
            pos += 3

    elif codeOp == saltarSiFalse:
        [variable,destino] = calcular2Param(pos,paramCode)
        if variable == 0:
            pos = destino
        else:
            pos += 3

    elif codeOp == menor:
        [operando1,operando2,destino] = calcular3Param(pos,paramCode)
        if operando1 < operando2:
            cinta[destino] = 1
        else:
            cinta[destino] = 0
        pos += 4

    elif codeOp == igual:
        [operando1,operando2,destino] = calcular3Param(pos,paramCode)
        if operando1 < operando2:
            cinta[destino] = 1
        else:
            cinta[destino] = 0
        pos += 4
    else:
        raise Exception('Code op at position %f is not correct. Code = %f',pos,cinta[pos])

