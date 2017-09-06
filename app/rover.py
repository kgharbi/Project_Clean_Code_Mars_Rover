import time
from app.commands import Command
from app.cardinal_directions import Direction
from app.planet_mars import PlanetMars

class Rover:
    isWorking = True

    XMIN = 0
    YMIN = 0
    XMAX = 9
    YMAX = 9

    mars = PlanetMars(10,10)

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def getPosition(self):
        return (self.x, self.y)

    def getOrientation(self):
        return (self.orientation)

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
            #time.sleep(0.5)
            print(self.createMapMars())

    def moveForward(self):
        if self.getOrientation() == Direction.NORTH:
            self.y += 1
            self.crossEdgeControl()
            if (self.mars.getCell(9 - self.x,self.y) == 'O'):
                self.y -= 1
                self.crossEdgeControl()
                self.stopWorking()




        elif self.getOrientation() == Direction.WEST:
            self.x -= 1
            self.crossEdgeControl()
            if (self.mars.getCell(9 - self.x,self.y) == 'O'):
                self.x += 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == Direction.SOUTH:
            self.y -= 1
            self.crossEdgeControl()
            if (self.mars.getCell(9 - self.x,self.y) == 'O'):
                self.y += 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == Direction.EST:
            self.x += 1
            self.crossEdgeControl()
            if (self.mars.getCell(9 - self.x, self.y) == 'O'):
                self.x -= 1
                self.crossEdgeControl()
                self.stopWorking()

    def moveBackward(self):
        if self.getOrientation() == Direction.NORTH:
            self.y -= 1
            self.crossEdgeControl()
            if (self.mars.getCell(9 - self.x, self.y) == 'O'):
                self.y += 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == Direction.WEST:
            self.x += 1
            self.crossEdgeControl()
            if (self.mars.getCell(9 - self.x,self.y) == 'O'):
                self.x -= 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == Direction.SOUTH:
            self.y += 1
            self.crossEdgeControl()
            if (self.mars.getCell(9 - self.x,self.y) == 'O'):
                self.y -= 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == Direction.EST:
            self.x -= 1
            self.crossEdgeControl()
            if (self.mars.getCell(9 - self.x,self.y) == 'O'):
                self.x += 1
                self.crossEdgeControl()
                self.stopWorking()

    def turnsLeft(self):
        if self.getOrientation() == Direction.NORTH:
            self.orientation = Direction.WEST
        elif self.getOrientation() == Direction.WEST:
            self.orientation = Direction.SOUTH
        elif self.getOrientation() == Direction.SOUTH:
            self.orientation = Direction.EST
        elif self.getOrientation() == Direction.EST:
            self.orientation = Direction.NORTH

    def turnsRight(self):
        if self.getOrientation() == Direction.NORTH:
            self.orientation = Direction.EST
        elif self.getOrientation() == Direction.WEST:
            self.orientation = Direction.NORTH
        elif self.getOrientation() == Direction.SOUTH:
            self.orientation = Direction.WEST
        elif self.getOrientation() == Direction.EST:
            self.orientation = Direction.SOUTH

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
        self.mars.addObstacle(0,9)
        self.mars.addRover(5,5)
        for i in range(self.XMAX + 1):
            for j in range(self.YMAX + 1):
                if (self.mars.getCell(i,j) != 'O'):
                    if (self.x == i and self.y == j):
                        map_mars += 'R'
                    else:
                        map_mars += '.'
                else:
                    map_mars += 'O'
            map_mars += '\n'
        return map_mars
