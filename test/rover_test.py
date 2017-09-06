from app.rover import Rover
from app.commands import Command


class RoverTest:
    def test_that_it_returns_coordinates(self):
        # given
        rover = Rover(0, 0, 'N')

        # that
        assert rover.getPosition() == (0, 0)

    def test_that_it_returns_orientation(self):
        # given
        rover = Rover(0, 0, 'N')

        # then
        assert rover.getOrientation() == 'N'

    def test_that_it_rolls_forward_when_it_receives_f_commmand_and_is_oriented_north(self):
        # given
        rover = Rover(5, 5, 'N')
        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (5, 6)

    def test_that_it_rolls_forward_when_it_receives_f_commmand_and_is_oriented_south(self):
        # given
        rover = Rover(5, 5, 'S')
        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (5, 4)

    def test_that_it_rolls_forward_when_it_receives_f_commmand_and_is_oriented_west(self):
        # given
        rover = Rover(5, 5, 'W')
        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (4, 5)

    def test_that_it_rolls_forward_when_it_receives_f_commmand_and_is_oriented_est(self):
        # given
        rover = Rover(5, 5, 'E')
        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (6, 5)

    def test_that_it_rolls_backward_when_it_receives_b_commmand_and_is_oriented_north(self):
        # given
        rover = Rover(5, 5, 'N')
        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (5, 4)

    def test_that_it_rolls_backward_when_it_receives_b_commmand_and_is_oriented_south(self):
        # given
        rover = Rover(5, 5, 'S')
        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (5, 6)

    def test_that_it_rolls_backward_when_it_receives_b_commmand_and_is_oriented_west(self):
        # given
        rover = Rover(5, 5, 'W')
        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (6, 5)

    def test_that_it_rolls_backward_when_it_receives_b_commmand_and_is_oriented_est(self):
        # given
        rover = Rover(5, 5, 'E')
        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (4, 5)

    def test_that_it_turns_left_when_it_receives_l_commmand_and_is_oriented_south(self):
        # given
        rover = Rover(5, 5, 'S')
        command_list = []
        command_list.append(Command.LEFT)

        # when
        rover.move(command_list)

        # then
        assert rover.getOrientation() == ('E')

    def test_that_it_turns_left_when_it_receives_l_commmand_and_is_oriented_north(self):
        # given
        rover = Rover(5, 5, 'N')
        command_list = []
        command_list.append(Command.LEFT)

        # when
        rover.move(command_list)

        # then
        assert rover.getOrientation() == ('W')

    def test_that_it_turns_left_when_it_receives_l_commmand_and_is_oriented_est(self):
        # given
        rover = Rover(5, 5, 'E')
        command_list = []
        command_list.append(Command.LEFT)

        # when
        rover.move(command_list)

        # then
        assert rover.getOrientation() == ('N')

    def test_that_it_turns_left_when_it_receives_l_commmand_and_is_oriented_west(self):
        # given
        rover = Rover(5, 5, 'W')
        command_list = []
        command_list.append(Command.LEFT)

        # when
        rover.move(command_list)

        # then
        assert rover.getOrientation() == ('S')

    def test_that_it_turns_right_when_it_receives_r_commmand_and_is_oriented_south(self):
        # given
        rover = Rover(5, 5, 'S')
        command_list = []
        command_list.append(Command.RIGHT)

        # when
        rover.move(command_list)

        # then
        assert rover.getOrientation() == ('W')

    def test_that_it_turns_right_when_it_receives_r_commmand_and_is_oriented_north(self):
        # given
        rover = Rover(5, 5, 'N')

        command_list = []
        command_list.append(Command.RIGHT)

        # when
        rover.move(command_list)

        # then
        assert rover.getOrientation() == ('E')

    def test_that_it_turns_right_when_it_receives_r_commmand_and_is_oriented_west(self):
        # given
        rover = Rover(5, 5, 'W')

        command_list = []
        command_list.append(Command.RIGHT)

        # when
        rover.move(command_list)

        # then
        assert rover.getOrientation() == ('N')

    def test_that_it_turns_right_when_it_receives_r_commmand_and_is_oriented_est(self):
        # given
        rover = Rover(5, 5, 'E')

        command_list = []
        command_list.append(Command.RIGHT)

        # when
        rover.move(command_list)

        # then
        assert rover.getOrientation() == ('S')

    def test_that_it_can_roll_over_forward_from_one_edge_of_the_grid_to_another_and_is_oriented_nord(self):
        # given
        rover = Rover(5, 9, 'N')

        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (5, 0)

    def test_that_it_can_roll_over_forward_from_one_edge_of_the_grid_to_another_and_is_oriented_sud(self):
        # given
        rover = Rover(5, 0, 'S')

        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (5, 9)

    def test_that_it_can_roll_over_forward_from_one_edge_of_the_grid_to_another_and_is_oriented_west(self):
        # given
        rover = Rover(0, 5, 'W')

        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (9, 5)

    def test_that_it_can_roll_over_forward_from_one_edge_of_the_grid_to_another_and_is_oriented_est(self):
        # given
        rover = Rover(9, 5, 'E')

        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (0, 5)

    def test_that_it_can_roll_over_backward_from_one_edge_of_the_grid_to_another_and_is_oriented_nord(self):
        # given
        rover = Rover(5, 0, 'N')

        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (5, 9)

    def test_that_it_can_roll_over_backward_from_one_edge_of_the_grid_to_another_and_is_oriented_sud(self):
        # given
        rover = Rover(5, 9, 'S')

        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (5, 0)

    def test_that_it_can_roll_over_backward_from_one_edge_of_the_grid_to_another_and_is_oriented_west(self):
        # given
        rover = Rover(9, 5, 'W')

        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (0, 5)

    def test_that_it_can_roll_over_backward_from_one_edge_of_the_grid_to_another_and_is_oriented_est(self):
        # given
        rover = Rover(0, 5, 'E')

        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (9, 5)

    def test_that_dont_move_forward_oriented_north_when_there_is_an_obstacle(self):
        # given
        rover = Rover(9, 8, 'N')

        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (9, 8)

    def test_that_dont_move_forward_oriented_south_when_there_is_an_obstacle(self):
        # given
        rover = Rover(9, 0, 'S')

        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (9, 0)

    def test_that_dont_move_forward_oriented_west_when_there_is_an_obstacle(self):
        # given
        rover = Rover(0, 9, 'W')

        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (0, 9)

    def test_that_dont_move_forward_oriented_est_when_there_is_an_obstacle(self):
        # given
        rover = Rover(8, 9, 'E')

        command_list = []
        command_list.append(Command.FORWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (8, 9)

    def test_that_dont_move_backward_oriented_north_when_there_is_an_obstacle(self):
        # given
        rover = Rover(9, 0, 'N')

        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (9, 0)

    def test_that_dont_move_backward_oriented_south_when_there_is_an_obstacle(self):
        # given
        rover = Rover(9, 8, 'S')

        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (9, 8)

    def test_that_dont_move_backward_oriented_west_when_there_is_an_obstacle(self):
        # given
        rover = Rover(8, 9, 'W')

        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (8, 9)

    def test_that_dont_move_backward_oriented_est_when_there_is_an_obstacle(self):
        # given
        rover = Rover(0, 9, 'E')

        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getPosition() == (0, 9)

    def test_that_should_stop_after_encountering_an_obstacle(self):
        # given
        rover = Rover(0, 9, 'E')

        command_list = []
        command_list.append(Command.BACKWARD)

        # when
        rover.move(command_list)

        # then
        assert rover.getWorking() == False

    def test_that_show_mars_with_obstacle_and_rover_position(self):
        # given
        rover = Rover(5, 5, 'E')

        # when
        rover.createMapMars()

        # then
        assert rover.createMapMars() == \
               '.........O\n' \
               + '..........\n' \
               + '..........\n' \
               + '..........\n' \
               + '..........\n' \
               + '.....R....\n' \
               + '..........\n' \
               + '..........\n' \
               + '..........\n' \
               + '..........\n'
