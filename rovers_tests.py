import unittest
from rovers import martian_robots


class TestRobots(unittest.TestCase):
    def setUp(self):
        self.data = [
            [
                "5 3",
                "1 1 E", "RFRFRFRF",
                "3 2 N", "FRRFLLFFRRFLL",
                "0 3 W", "LLFFFLFLFL"
            ],
            [
                "0 0",
                "0 0 N", "F"
            ],
            [
                "5 5",
                "3 4 N", "LRLRLLLRRRLLR"
            ],
            [
                "6 6",
                "2 5 S", "FFFFF"
            ],
            [
                "50 50",
                "45 2 E", "LFLFLFLFFRRFFFRLRLLFFR",
                "15 24 W", "LRFFFLLRFFLRFRFLLFRRLLF"
            ]
        ]

    def test_travelling_rover(self):
        """
        Test given test case for robots challenge.
        """

        self.assertEqual(martian_robots(
            self.data[0]),
            '1 1 E\n3 3 N LOST\n3 3 N LOST'
        )

    def test_nonexistant_grid(self):
        """
        Test the edge case when the grid is 0 by 0 (nonexistant).
        """

        self.assertEqual(martian_robots(
            self.data[1]),
            '0 0 N LOST'
        )

    def test_rotate_only(self):
        """
        Test rotation only.
        """

        self.assertEqual(martian_robots(
            self.data[2]),
            '3 4 W'
        )

    def test_move_only(self):
        """
        Test movement only.
        """

        self.assertEqual(martian_robots(
            self.data[3]),
            '2 0 S'
        )

    def test_travelling_rover2(self):
        """
        Test on large given grid.
        """

        self.assertEqual(martian_robots(
            self.data[4]),
            '43 0 W\n13 21 E'
        )
