def execute_sequence():



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

    result = [[(3, 3), 'N']]
    """

    width, height = list(map(lambda k: int(k), data[0].split(" ")))
    end_positions = []

    for robot in range(1, len(data), 2):

        start_x, start_y, direction = data[robot].split(" ")
        commands = data[robot + 1]

        end_sequence.append(
            execute_commands(
                start_x,
                start_y,
                direction,
                commands,
                width,
                height
            )
        )

    return end_positions