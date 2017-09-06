import numpy as np

class PlanetMars:

    def __init__(self, planet_size_x, planet_size_y):
        self.planet_size_x = planet_size_x
        self.planet_size_y = planet_size_y
        self.mars = np.empty((planet_size_x,planet_size_y), dtype=str)

    def getPlanetDimension(self):
        return self.mars.shape

    def getCell(self, position_x, position_y):
        return self.mars[position_x][position_y]

    def addObstacle(self, position_x, position_y):
        self.mars[position_x][position_y] = 'O'

    def addRover(self, position_x, position_y):
        self.mars[position_x][position_y] = 'R'








