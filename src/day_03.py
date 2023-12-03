# Standard Library
import re
from collections import defaultdict
from itertools import product

# First Party
from utils import no_input_skip, read_input


def part_1(input: str) -> int:
    regex = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    cloth = defaultdict(int)
    for line in input.splitlines():
        if (match := regex.search(line)) is not None:
            _, l, t, w, h = map(int, match.groups())
            for x, y in product(range(l, l + w), range(t, t + h)):
                cloth[x, y] += 1

    return sum(1 for c in cloth.values() if c > 1)


def part_2(input: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""


def test_part_1():
    test_input = get_example_input()
    assert part_1(test_input) == 4


# def test_part_2():
#     test_input = get_example_input()
#     assert part_2(test_input) is not None


@no_input_skip
def test_part_1_real():
    real_input = read_input(__file__)
    assert part_1(real_input) == 112378


# @no_input_skip
# def test_part_2_real():
#     real_input = read_input(__file__)
#     assert part_2(real_input) is not None


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
