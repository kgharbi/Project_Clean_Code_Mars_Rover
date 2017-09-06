import numpy as np

class PlanetMars:

    def __init__(self, planet_size_x, planet_size_y):
        self.planet_size_x = planet_size_x
        self.planet_size_y = planet_size_y
        self.mars = np.empty((planet_size_x,planet_size_y), dtype=str)

    def getPlanetDimension(self):
        print(self.mars)
        return self.mars.shape


