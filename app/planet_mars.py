import numpy as np


class PlanetMars:
    XMIN = 0
    YMIN = 0
    XMAX = 9
    YMAX = 9

    def __init__(self, planet_size_x, planet_size_y):
        self.planet_size_x = planet_size_x
        self.planet_size_y = planet_size_y
        self.mars = np.empty((planet_size_x, planet_size_y), dtype=str)

    def getPlanetDimension(self):
        return self.mars.shape

    def getCell(self, position_x, position_y):
        return self.mars[position_x][position_y]

    def addObstacle(self, position_x, position_y):
        self.mars[position_x][position_y] = 'O'

    def addRover(self, position_x, position_y):
        self.mars[position_x][position_y] = 'R'

    def isTileFree(self, newCoordinatesX, newCoordinatesY):

        if newCoordinatesX >= self.XMAX + 1:
            newCoordinatesX = self.XMIN
        if newCoordinatesY >= self.YMAX + 1:
            newCoordinatesY = self.YMIN
        if newCoordinatesX <= self.XMIN - 1:
            newCoordinatesX = self.XMAX
        if newCoordinatesY <= self.YMIN - 1:
            newCoordinatesY = self.YMAX

        planetCoordX = 9 - newCoordinatesX
        planetCoordY = newCoordinatesY

        print ("A", self.getCell(planetCoordX, planetCoordY) == '')

        return (self.getCell(planetCoordX, planetCoordY) == '')
