# Standard Library
from itertools import accumulate, cycle

# First Party
from utils import no_input_skip, read_input


def part_1(input: str) -> int:
    return sum(map(int, input.splitlines()))


def part_2(input: str) -> int:
    changes = map(int, input.splitlines())
    history: set[int] = set()
    for freq in accumulate(cycle(changes)):
        if freq in history:
            return freq
        history.add(freq)

    raise Exception("This can't happen")


# -- Tests


def get_example_input() -> str:
    return """+1
-2
+3
+1"""


def test_part_1():
    test_input = get_example_input()
    assert part_1(test_input) == 3


def test_part_2():
    test_input = get_example_input()
    assert part_2(test_input) == 2


@no_input_skip
def test_part_1_real():
    real_input = read_input(__file__)
    assert part_1(real_input) == 520


@no_input_skip
def test_part_2_real():
    real_input = read_input(__file__)
    assert part_2(real_input) == 394


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
