def manhatan(posCable):
    
    distance = abs(posCable.getCoordX()) + abs(posCable.getCoordY())
    return distance

def minDist(interseccionCables):

    posMin = interseccionCables[0]
    minimo = manhatan(dev.getCoordX(),dev.getCoordY())

    for posCable in lista:
        distancia = manhatan(posCable)
        if distancia < minimo:
            minimo = distancia
            posMin = posCable
    return minimo

from Clasesday3 import Cable,PosCable
fh = open('input.txt','r')
datosEntrada = []

for line in fh:
    line = line.rstrip('\n')
    line = line.rsplit(',')
    datosEntrada.append(line)
    
cable1 = Cable(datosEntrada[0])

cable2 = Cable(datosEntrada[1])

cable1.calcularCamino()
cable2.calcularCamino()

interseccionCables = cable1.interseccion(cable2)

distancia = minDist(interseccionCables)

print(distancia)