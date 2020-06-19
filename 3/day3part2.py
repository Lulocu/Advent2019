def calcularListaX(origen,movimiento,resta,nPasos):
    res = []

    for aux in range(movimiento + 1):
        
        if resta:
            tup = (origen[0],origen[1] - aux,nPasos)
        else:
            tup = (origen[0],origen[1] + aux,nPasos)
        res.append(tup)
        nPasos+=1
    return res


def calcularListaY(origen,movimiento,resta,nPasos):
    res = []
    for aux in range(movimiento + 1):
        
        if resta:
            tup = (origen[0]-aux,origen[1],nPasos)
        else:
            tup = (origen[0]+aux,origen[1],nPasos)
        res.append(tup)
        nPasos+=1
    return res

def interseccion(cable1,cable2):
    res = []
    for pos in cable1:
        for elemento in cable2:
            if pos[0] == elemento[0] and pos[1] == elemento[1]:
                res.append((pos[0],pos[1],pos[2]+elemento[2]))
                
    return res

def buscarMenor(lista):

    dev = lista[0]
    dist = lista[0][2]

    for element in lista:
        aux = element[2]
        if aux < dist:
            dist = aux
            dev = element
    return dist

pos = (0,0,0)
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
    for movimiento in dicc[cable]: #['R23' 'u63']
        direccion = movimiento[0]
        cantidad = int(movimiento[1:])
        origen = camino[cable][-1]

        if direccion == 'R':
            
            nuevo = calcularListaX(origen,cantidad,False,origen[2])
            
        elif direccion == 'L':
            nuevo = calcularListaX(origen,cantidad,True,origen[2])

        elif direccion == 'U':
            nuevo = calcularListaY(origen,cantidad,False,origen[2])

        elif direccion == 'D':
            nuevo = calcularListaY(origen,cantidad,True,origen[2])
            
        else:
            raise Exception('Direccion desconocida '+ direccion)

        camino[cable] = camino[cable] + nuevo

camino[1].remove((0,0,0))
camino[1].remove((0,0,0))
res = interseccion(camino[1],camino[2])

distancia = buscarMenor(res)

print(distancia)