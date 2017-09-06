from app.compass import Compass
from app.cardinal_directions import Direction


class CompassTest:
    def test_compass_should_initialise(self):
        compass = Compass(Direction.NORTH)
        assert compass.getDirection() == Direction.NORTH


    def test_compass_should_turn_left_correctly_when_its_north(self):
        compass = Compass(Direction.NORTH)
        compass.rotate90Clockwise()
        assert compass.getDirection() == Direction.WEST

    def test_compass_should_turn_left_correctly_when_its_west(self):
        compass = Compass(Direction.WEST)
        compass.rotate90Clockwise()
        assert compass.getDirection() == Direction.SOUTH

    def test_compass_should_turn_left_correctly_when_its_south(self):
        compass = Compass(Direction.SOUTH)
        compass.rotate90Clockwise()
        assert compass.getDirection() == Direction.EST

    def test_compass_should_turn_left_correctly_when_its_est(self):
        compass = Compass(Direction.EST)
        compass.rotate90Clockwise()
        assert compass.getDirection() == Direction.NORTH

    def test_compass_should_turn_right_correctly_when_its_north(self):
        compass = Compass(Direction.NORTH)
        compass.rotate90CounterClockwise()
        assert compass.getDirection() == Direction.EST

    def test_compass_should_turn_right_correctly_when_its_est(self):
        compass = Compass(Direction.EST)
        compass.rotate90CounterClockwise()
        assert compass.getDirection() == Direction.SOUTH

    def test_compass_should_turn_right_correctly_when_its_south(self):
        compass = Compass(Direction.SOUTH)
        compass.rotate90CounterClockwise()
        assert compass.getDirection() == Direction.WEST

    def test_compass_should_turn_right_correctly_when_its_west(self):
        compass = Compass(Direction.WEST)
        compass.rotate90CounterClockwise()
        assert compass.getDirection() == Direction.NORTH