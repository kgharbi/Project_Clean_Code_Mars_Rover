from app.cardinal_directions import Direction


class Compass:
    clockwise = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EST]

    currentDirection = Direction.NORTH

    def __init__(self, direction):
        self.currentDirection = direction

    def rotate90Clockwise(self):
        self.currentDirection = self.clockwise[(self.clockwise.index(self.currentDirection) + 1) % 4]

    def rotate90CounterClockwise(self):
        self.currentDirection = self.clockwise[(self.clockwise.index(self.currentDirection) - 1) % 4]

    def getDirection(self):
        return self.currentDirection
