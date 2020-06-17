def calcularListaX(origen,movimiento,resta):
    res = []
    
    for aux in range(movimiento + 1):
        if resta:
            tup = (origen[0],origen[1] - aux)
        else:
            tup = (origen[0],origen[1] + aux)
        res.append(tup)
    return res


def calcularListaY(origen,movimiento,resta):
    res = []
    
    for aux in range(movimiento + 1):
        if resta:
            tup = (origen[0]-aux,origen[1])
        else:
            tup = (origen[0]+aux,origen[1])
        res.append(tup)
    return res

def manhatan(x,y):
  #  print(x,y)
    
    distance = abs(x - 0) + abs(y - 0)
  #  print(distance)
    return distance
def calcularListaXNPasos(origen,movimiento,resta):
    res = []
    
    for aux in range(movimiento + 1):
        if resta:
            tup = (origen[0],origen[1] - aux)
        else:
            tup = (origen[0],origen[1] + aux)
        res.append(tup)
    return res


def calcularListaYNPasos(origen,movimiento,resta):
    res = []
    
    for aux in range(movimiento + 1):
        if resta:
            tup = (origen[0]-aux,origen[1])
        else:
            tup = (origen[0]+aux,origen[1])
        res.append(tup)
    return res
    
def busqNPasos(pos):
    pasos = 0
    for cable in dicc.keys():
        for movimiento in dicc[cable]:
            origen = camino[cable][-1]
            if origen == pos:
                break
            pasos = pasos + 1
            direccion = movimiento[0]
            cantidad = int(movimiento[1:])
            if direccion == 'R':
                nuevo = calcularListaX(origen,cantidad,False)

            elif direccion == 'L':
                nuevo = calcularListaX(origen,cantidad,True)

            elif direccion == 'U':
                nuevo = calcularListaY(origen,cantidad,False)

            elif direccion == 'D':
                nuevo = calcularListaY(origen,cantidad,True)
                
            else:
                raise Exception('Direccion desconocida '+ direccion)

            camino[cable] = camino[cable] + nuevo
    return pasos



pos = (0,0)
fh = open('input.txt','r')
cont = 1
dicc = {}
for line in fh:
    line = line.rstrip('\n')
    line = line.rsplit(',')
    dicc[cont] =line
    cont+=1

camino = {1:[pos],2:[pos]}

for cable in dicc.keys():
    for movimiento in dicc[cable]:

        origen = camino[cable][-1]
        direccion = movimiento[0]
        cantidad = int(movimiento[1:])

        if direccion == 'R':
            nuevo = calcularListaX(origen,cantidad,False)

        elif direccion == 'L':
            nuevo = calcularListaX(origen,cantidad,True)

        elif direccion == 'U':
            nuevo = calcularListaY(origen,cantidad,False)

        elif direccion == 'D':
            nuevo = calcularListaY(origen,cantidad,True)

        else:
            raise Exception('Direccion desconocida '+ direccion)

        camino[cable] = camino[cable] + nuevo

res = list(set(camino[1]) & set(camino[2]))

res.remove((0,0))
dev = None
dist = 999999
for element in res:


    aux = busqNPasos(element)
    if aux < dist:
        print('dentro')
        dist = aux
        dev = element
print(dist)