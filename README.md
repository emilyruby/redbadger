# Red Badger Coding Challenge

This respository contains the code and tests for the Red Badger Coding Challenge.

`rovers.py` contains the implementation of the algorithm.

`tests.py` contains the tests for this solution, considering edge cases.

You can pass data to the `martian_robots` function in the format:

```
[
    "5 3",
    "1 1 E", "RFRFRFRF",
    "3 2 N", "FRRFLLFFRRFLL",
    "0 3 W", "LLFFFLFLFL"
]
```

Where the first element is a string representing the grid dimensions. The next 2 elements represent the start co-ordinates and orientation of the first robot, and then the sequence of instructions for it to follow. The next 2 elements represent the next robot and so-on. 