from app.planet_mars import PlanetMars


class PlanetMarsTest:
    def test_that_it_returns_a_2D_planet_array(self):
        # given
        mars = PlanetMars(10, 10)

        # that
        assert mars.getPlanetDimension() == (10, 10)
