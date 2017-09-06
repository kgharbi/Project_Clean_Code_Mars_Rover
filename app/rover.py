import time
from commands import Command

class Rover:
    isWorking = True

    XMIN = 0
    YMIN = 0
    XMAX = 9
    YMAX = 9

    mars_grid = [[False, False, False, False, False, False, False, False, False, True],
                 [False, False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False, False]]

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
            time.sleep(0.5)
            print(self.createMapMars())

    def moveForward(self):
        if self.getOrientation() == 'N':
            self.y += 1
            self.crossEdgeControl()
            if (self.mars_grid[9 - self.x][self.y] == True):
                self.y -= 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == 'W':
            self.x -= 1
            self.crossEdgeControl()
            if (self.mars_grid[9 - self.x][self.y] == True):
                self.x += 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == 'S':
            self.y -= 1
            self.crossEdgeControl()
            if (self.mars_grid[9 - self.x][self.y] == True):
                self.y += 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == 'E':
            self.x += 1
            self.crossEdgeControl()
            if (self.mars_grid[9 - self.x][self.y] == True):
                self.x -= 1
                self.crossEdgeControl()
                self.stopWorking()

    def moveBackward(self):
        if self.getOrientation() == 'N':
            self.y -= 1
            self.crossEdgeControl()
            if (self.mars_grid[9 - self.x][self.y] == True):
                self.y += 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == 'W':
            self.x += 1
            self.crossEdgeControl()
            if (self.mars_grid[9 - self.x][self.y] == True):
                self.x -= 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == 'S':
            self.y += 1
            self.crossEdgeControl()
            if (self.mars_grid[9 - self.x][self.y] == True):
                self.y -= 1
                self.crossEdgeControl()
                self.stopWorking()
        elif self.getOrientation() == 'E':
            self.x -= 1
            self.crossEdgeControl()
            if (self.mars_grid[9 - self.x][self.y] == True):
                self.x += 1
                self.crossEdgeControl()
                self.stopWorking()

    def turnsLeft(self):
        if self.getOrientation() == 'N':
            self.orientation = 'W'
        elif self.getOrientation() == 'W':
            self.orientation = 'S'
        elif self.getOrientation() == 'S':
            self.orientation = 'E'
        elif self.getOrientation() == 'E':
            self.orientation = 'N'

    def turnsRight(self):
        if self.getOrientation() == 'N':
            self.orientation = 'E'
        elif self.getOrientation() == 'W':
            self.orientation = 'N'
        elif self.getOrientation() == 'S':
            self.orientation = 'W'
        elif self.getOrientation() == 'E':
            self.orientation = 'S'

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
        for i in range(self.XMAX + 1):
            for j in range(self.YMAX + 1):
                if self.mars_grid[i][j] == False:
                    if (self.x == i and self.y == j):
                        map_mars += 'R'
                    else:
                        map_mars += '.'
                else:
                    map_mars += 'O'

            map_mars += '\n'
        return map_mars
