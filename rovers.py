def execute_sequence(start_x, start_y, direction, sequence, width, height):
    """
    INPUT: Start coordinates of robot, direction facing at beginning,
    sequence of commands, then the width and height of the grid.

    OUTPUT: The final position and orientation of the robot in the format:

    result = [[(3, 3), 'N']]
    """

    dirs = ["N", "E", "S", "W"]
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

    current_x, current_y = int(start_x), int(start_y)
    current_dir = direction

    for ins in sequence:

        previous_x, previous_y = current_x, current_y
        if ins == "F":
            current_x += moves[current_dir][0]
            current_y += moves[current_dir][1]
        else:
            current_dir_index = (dirs.index(current_dir) + turn_map[ins]) % 4
            current_dir = dirs[current_dir_index]
        if not (0 <= current_x <= width and 0 <= current_y <= height):
            return str([(previous_x, previous_y), current_dir] + 'LOST')

    return str([(current_x, current_y), current_dir])


def change_input(a):
    return list(map(lambda k: int(k), a))


def martian_robots(data):
    """
    INPUT: Presume data structure for now is structure such as:

    data = [
        "5 3",
        "1 1 E", "RFRFRFRF",
        "3 2 N", "FRRFLLFFRRFLL"
        and so on
    ]

    OUTPUT: Coordinates of finishing point, plus orientation in format:

    result = [[(3, 3), 'N']] for each robot.
    """

    width, height = change_input(data[0].split(" "))
    end_positions = []

    for robot in range(1, len(data), 2):

        *start, direction = data[i].split(" ")
        start = change_input(start)
        sequence = data[robot + 1]

        end_sequence.append(
            execute_commands(
                start_x,
                start_y,
                direction,
                sequence,
                width,
                height
            )
        )

    return end_positions