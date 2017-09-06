from app.planet_mars import PlanetMars


class PlanetMarsTest:
    def test_that_it_returns_a_2D_planet_array(self):
        # given
        mars = PlanetMars(10, 10)

        # that
        assert mars.getPlanetDimension() == (10, 10)

    def test_that_it_gets_a_cell_of_planet_mars(self):
        #given
        mars = PlanetMars(10, 10)

        # that
        assert mars.getCell(0, 0) == ''

    def test_that_an_obstacle_can_be_added_on_the_planet(self):
        #given
        mars = PlanetMars(10,10)

        #when
        mars.addObstacle(9,9)

        #then
        assert mars.getCell(9, 9) == 'O'

    def test_that_it_adds_a_rover_to_planet_mars(self):
        # given
        mars = PlanetMars(10, 10)

        # when
        mars.addRover(5, 5)

        # that
        assert mars.getCell(5, 5) == 'R'
