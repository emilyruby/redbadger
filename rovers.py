def return_string(values):
    return " ".join(list(map(lambda k: str(k), values)))


def execute_sequence(start, direction, sequence, width, height):

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
    return list(map(lambda k: int(k), a))


def martian_robots(data):
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
