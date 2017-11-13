def return_string(values):
    """
    Input: List of values representing the position of the robot.

    Output: Formatted string of robot position, for example:

    'X Y DIRECTION (LOST)'
    """

    return " ".join(list(map(lambda k: str(k), values)))


def execute_sequence(start, direction, sequence, width, height):
    """
    Input:  Start co-ordinates, starting orientation, sequence of commands,
            width of grid, height of grid.
    Output: String representing the end position and orientation of the robot
            in the format:

    'X Y DIRECTION (LOST)'

    Lost is appended to the string if the robot at any point leaves the grid.
    """

    dirs = ["N", "E", "S", "W"]
    TOTAL_DIRECTIONS = len(dirs)
    turn_map = {
        "R": 1,
        "L": -1
    }
    moves = {
        "N": [0, 1],
        "S": [0, -1],
        "E": [1, 0],
        "W": [-1, 0]
    }

    current_x, current_y = start
    current_dir = direction

    for cmd in sequence:

        previous_x, previous_y = current_x, current_y

        if cmd == "F":
            current_x += moves[current_dir][0]
            current_y += moves[current_dir][1]
        else:
            current_dir_index = (dirs.index(current_dir) + turn_map[cmd]) % TOTAL_DIRECTIONS
            current_dir = dirs[current_dir_index]

        if not (0 <= current_x <= width and 0 <= current_y <= height):
            return return_string([previous_x, previous_y, current_dir, 'LOST'])

    return return_string((current_x, current_y, current_dir))


def modify_input(a):
    """
    Input: List of strings/characters.
    Output: List of integers.
    """

    return list(map(lambda k: int(k), a))


def martian_robots(data):
    """
    Input: Data representing the task, in the format (for example):

    [
        "GRID_WIDTH GRID_HEIGHT",
        "X Y DIRECTION", "SEQUENCE OF COMMANDS",
        "3 2 N", "FRRFLLFFRRFLL"
    ]

    Output: A string representing the end positions of all robots in the data
            (separated by a new line).
    """

    width, height = modify_input(data[0].split(" "))
    end_positions = []

    for i in range(1, len(data), 2):

        *start, direction = data[i].split(" ")
        start = modify_input(start)
        sequence = data[i + 1]

        end_positions.append(
            execute_sequence(start, direction, sequence, width, height)
        )

    return "\n".join(end_positions)
