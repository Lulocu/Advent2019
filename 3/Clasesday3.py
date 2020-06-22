class PosCable:
    #def __init__(self,coordX,coordY):
    #    self.coordX = coordX
    #    self.coordY = coordY
    #    self.distancia = None

    def __init__(self,coordX,coordY,distancia = None):
        self.coordX = coordX
        self.coordY = coordY
        self.distancia = distancia

    #getters
    def getCoordX(self):
        return self.coordX
    def getCoordY(self):
        return self.coordY
    def getDistancia(self):
        return self.distancia
        
    #setters
    def setCoordX(self,newCoordX):
        self.coordX = newCoordX
    def setCoordY(self,newCoordY):
        self.coordY = newCoordY
    def setDistancia(self,newDistancia):
        self.distancia = newDistancia

class Cable:
    def __init__(self,instrucciones):
        self.instrucciones = instrucciones
        origen = PosCable(0,0)
        self.camino = [origen]

    #getters
    def getCamino(self):
        return self.camino
    def getInstrucciones(self):
        return self.instrucciones

    #Calcular ejes
    def calcularXPositivas(cantidad):
        for i in range(cantidad):
            origen = self.getCamino[-1]
            nuevaPosCable = PosCable(origen.getCoordX() + 1, origen.getCoordY())
            self.camino.append(nuevaPosCable)

    def calcularXNegativas(cantidad):
        for i in range(cantidad):
            origen = self.getCamino[-1]
            nuevaPosCable = PosCable(origen.getCoordX() - 1, origen.getCoordY())
            self.camino.append(nuevaPosCable)

    def calcularYPositivas(cantidad):
        for i in range(cantidad):
            origen = self.getCamino[-1]
            nuevaPosCable = PosCable(origen.getCoordX(), origen.getCoordY() + 1)
            self.camino.append(nuevaPosCable)

    def calcularYPositivas(cantidad):
    
        for i in range(cantidad):
            origen = self.getCamino[-1]
            nuevaPosCable = PosCable(origen.getCoordX(), origen.getCoordY() - 1)
            self.camino.append(nuevaPosCable)
    def calcularCamino(self):
        instrucciones = self.getInstrucciones()
        for instruccion in instrucciones:
            direccion = instruccion[0]
            cantidad = int(instruccion[1:])
            if direccion == 'R':
                nuevo = calcularXPositivas(cantidad)

            elif direccion == 'L':
                nuevo = calcularXNegativas(cantidad)

            elif direccion == 'U':
                nuevo = calcularYPositivas(cantidad)

            elif direccion == 'D':
                nuevo = calcularYNegativas(cantidad)

            else:
                raise Exception('Direccion desconocida '+ direccion)
            self.camino.append(nuevo)



    def interseccion(self,cable):
        res = list(set(self.getCamino()) & set(cable.getCamino()))
        origen = PosCable(0,0)
        res.remove(origen)
        return res