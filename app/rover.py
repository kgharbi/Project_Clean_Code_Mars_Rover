import time
from app.commands import Command
from app.cardinal_directions import Direction
from app.compass import Compass
from app.planet_mars import PlanetMars


class Rover:

    isWorking = True
    compass = Compass
    XMIN = 0
    YMIN = 0
    XMAX = 9
    YMAX = 9
    mars = PlanetMars(10, 10)

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.compass = Compass(orientation)

    def getPosition(self):
        return (self.x, self.y)

    def move(self, command_list):
        for action in command_list:
            if action == Command.FORWARD:
                self.moveForward()
                self.crossEdgeControl()
            if action == Command.BACKWARD:
                self.moveBackward()
                self.crossEdgeControl()
            if action == Command.LEFT:
                self.turnsLeft()
            if action == Command.RIGHT:
                self.turnsRight()
            # time.sleep(0.5)
            print(self.createMapMars())

    def moveForward(self):
        newCoordinatesX = self.x
        newCoordinatesY = self.y

        if self.compass.getDirection() == Direction.NORTH:
            newCoordinatesY += 1
        elif self.compass.getDirection() == Direction.WEST:
            newCoordinatesX -= 1
        elif self.compass.getDirection() == Direction.SOUTH:
            newCoordinatesY -= 1
        elif self.compass.getDirection() == Direction.EST:
            newCoordinatesX += 1

        if (self.mars.isTileFree(newCoordinatesX, newCoordinatesY)):
            self.x = newCoordinatesX
            self.y = newCoordinatesY

        else:
            self.stopWorking()



    def moveBackward(self):

        newCoordinatesX = self.x
        newCoordinatesY = self.y

        if self.compass.getDirection() == Direction.NORTH:
            newCoordinatesY -= 1
        elif self.compass.getDirection() == Direction.WEST:
            newCoordinatesX += 1
        elif self.compass.getDirection() == Direction.SOUTH:
            newCoordinatesY += 1
        elif self.compass.getDirection() == Direction.EST:
            newCoordinatesX -= 1

        if (self.mars.isTileFree(newCoordinatesX, newCoordinatesY)):
            self.x = newCoordinatesX
            self.y = newCoordinatesY


        else:
            self.stopWorking()

    def turnsLeft(self):
        self.compass.rotate90Clockwise()

    def turnsRight(self):
        self.compass.rotate90CounterClockwise()

    def crossEdgeControl(self):
        if self.x == self.XMAX + 1:
            self.x = self.XMIN
        if self.y == self.YMAX + 1:
            self.y = self.YMIN
        if self.x == self.XMIN - 1:
            self.x = self.XMAX
        if self.y == self.YMIN - 1:
            self.y = self.YMAX

    def stopWorking(self):
        self.isWorking = False

    def getWorking(self):
        return self.isWorking

    def createMapMars(self):
        map_mars = ''
        self.mars.addObstacle(0, 9)
        self.mars.addRover(5, 5)
        for i in range(self.XMAX + 1):
            for j in range(self.YMAX + 1):
                if (self.mars.getCell(i, j) != 'O'):
                    if (self.x == i and self.y == j):
                        map_mars += 'R'
                    else:
                        map_mars += '.'
                else:
                    map_mars += 'O'
            map_mars += '\n'
        return map_mars

    def getOrientation(self):
        return self.compass.getDirection()
