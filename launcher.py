from app.rover import Rover
from app.commands import Command


rover = Rover(5, 5, 'E')
command_list = []
command_list.append(Command.FORWARD)
command_list.append(Command.FORWARD)
command_list.append(Command.FORWARD)
command_list.append(Command.FORWARD)
rover.move(command_list)