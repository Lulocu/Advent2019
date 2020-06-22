class PosCable:
    def __init__(self,coordX,coordY):
        self.coordX = coordX
        self.coordY = coordY
        self.distancia = None

    def __init__(self,coordX,coordY,distancia):
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