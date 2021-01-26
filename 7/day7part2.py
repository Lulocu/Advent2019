"""
Advent of code 2019 day 7 part2
"""  

import itertools
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
global nCeldilla
nCeldilla = 0
def iniciarCinta():
    fh = open("inputPrueba.txt",'r')
    global cinta
    cinta = fh.read()
    cinta = cinta.rsplit(',')
    cinta = list(map(int,cinta))

def calc1Param(nCeldilla,codeParam):
    codeParam = list(map(int, str(codeParam)))
    if len(codeParam) < 1:
        return cinta[cinta[nCeldilla + 1]]
    else:
        return cinta[nCeldilla+1]

def calc2Param(nCeldilla,codeParam):
    codeParam = list(map(int, str(codeParam)))
    if len(codeParam) < 2:
        codeParam.insert(0,0)

    if codeParam[-1] == 0:
        op = cinta[cinta[nCeldilla + 1]]
    else:
        op = cinta[nCeldilla+1]

    if codeParam[-2] == 0:
        dest = cinta[cinta[nCeldilla + 2]]
    else:
        dest = cinta[nCeldilla + 2]

    return[op, dest]

def calc3Param(nCeldilla,codeParam):
    codeParam = list(map(int, str(codeParam)))

    while len(codeParam) < 2:
        codeParam.insert(0,0)

    if codeParam[-1] != 1:
        op1 = cinta[cinta[nCeldilla + 1]]
    else:
        op1 = cinta[nCeldilla+1]

    if codeParam[-2] != 1:
        op2 = cinta[cinta[nCeldilla + 2]]
    else:
        op2 = cinta[nCeldilla + 2]

    dest =  cinta[nCeldilla + 3]
    return[op1, op2, dest]

def controlador(fase, input2):  
    global nCeldilla
    
    inputNumber = fase

    while nCeldilla < len(cinta):

        aux=str(cinta[nCeldilla])
        #int para evitar '01' != '1'
        codeOp = int(aux[-2:])
        codeParam = aux[0:-2]

        if codeOp == parar:
            stop = True
            break

        elif codeOp == sumar:
            [sum1, sum2, dest] = calc3Param(nCeldilla,codeParam)
            cinta[dest]  = sum1 + sum2
            nCeldilla += 4

        elif codeOp == multiplicar:
            [mult1, mult2,dest] = calc3Param(nCeldilla,codeParam)
            cinta[dest]  = mult1 * mult2
            nCeldilla += 4

        elif codeOp == entrada:
            cinta[cinta[nCeldilla+1]] = int(inputNumber)
            inputNumber = input2
            nCeldilla += 2

        elif codeOp == salida:
            dest = calc1Param(nCeldilla,codeParam)
            return(dest)
            nCeldilla += 2

        elif codeOp == saltarSiTrue:
            [op,dest] = calc2Param(nCeldilla,codeParam)
            if op != 0:
                nCeldilla = dest
            else:
                nCeldilla += 3

        elif codeOp == saltarSiFalse:
            [op,dest] = calc2Param(nCeldilla,codeParam)
            if op == 0:
                nCeldilla = dest
            else:
                nCeldilla += 3

        elif codeOp == menor:
            [op1,op2,dest] = calc3Param(nCeldilla,codeParam)
            if op1 < op2:
                cinta[dest] = 1
            else:
                cinta[dest] = 0
            nCeldilla += 4

        elif codeOp == igual:
            [op1,op2,dest] = calc3Param(nCeldilla,codeParam)
            if op1 == op2:
                cinta[dest] = 1
            else:
                cinta[dest] = 0
            nCeldilla += 4

        else:
            raise Exception('Code operation at Celdilla nº %f is not correct. Code = %f',nCeldilla, cinta[nCeldilla])



iniciarCinta()

resultados = []
#numeros = [5,6,7,8,9]
#permutaciones= list(itertools.permutations(numeros, 5))
permutaciones = [9,8,7,6,5]
stop = False
for i in range(1):#combinacion in permutaciones:
    combinacion = [9,8,7,6,5]
    inputAct = 0
    while not stop:
        for fase in combinacion:
            inputAct = controlador(fase,inputAct)
            i = i+1
           
    resultados = resultados + [inputAct]
    stop = False
print(max(resultados))
