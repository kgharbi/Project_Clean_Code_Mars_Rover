from app.rover import Rover
import sys


rover = Rover(5, 5, 'E')
command_list = 'fblrfffblllrff'
rover.move(command_list)