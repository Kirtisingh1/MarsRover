class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        print(f"Rover moved to ({self.x}, {self.y})")

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        print(f"Rover turned left. Now facing {self.direction}")

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        print(f"Rover turned right. Now facing {self.direction}")

    def report(self):
        print(f"Rover is at ({self.x}, {self.y}) facing {self.direction}")


# Command Pattern
class Command:
    def execute(self):
        pass


class MoveCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.move()


class TurnLeftCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_left()


class TurnRightCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_right()


# Simulation
if __name__ == "__main__":
    rover = Rover(0, 0, 'N')  # Start at (0, 0) facing North

    # Commands
    move_command = MoveCommand(rover)
    turn_left_command = TurnLeftCommand(rover)
    turn_right_command = TurnRightCommand(rover)

    # Simulating movements
    move_command.execute()  # Move forward
    turn_right_command.execute()  # Turn right
    move_command.execute()  # Move forward
    turn_left_command.execute()  # Turn left
    move_command.execute()  # Move forward

    # Reporting position
    rover.report()  # Rover is at (1, 2) facing N
