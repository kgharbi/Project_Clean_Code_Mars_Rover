import time

from app.const import Const as CONSTANT


class Rover:
    isWorking = True

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
            if action == 'f':
                self.moveForward()
                self.crossEdgeControl()
            if action == 'b':
                self.moveBackward()
                self.crossEdgeControl()
            if action == 'l':
                self.turnsLeft()
            if action == 'r':
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
        if self.x == CONSTANT.XMAX + 1:
            self.x = CONSTANT.XMIN
        if self.y == CONSTANT.YMAX + 1:
            self.y = CONSTANT.YMIN
        if self.x == CONSTANT.XMIN - 1:
            self.x = CONSTANT.XMAX
        if self.y == CONSTANT.YMIN - 1:
            self.y = CONSTANT.YMAX

    def stopWorking(self):
        self.isWorking = False

    def getWorking(self):
        return self.isWorking

    def createMapMars(self):
        map_mars = ''
        for i in range(CONSTANT.XMAX + 1):
            for j in range(CONSTANT.YMAX + 1):
                if self.mars_grid[i][j] == False:
                    if (self.x == i and self.y == j):
                        map_mars += 'R'
                    else:
                        map_mars += '.'
                else:
                    map_mars += 'O'

            map_mars += '\n'
        return map_mars
