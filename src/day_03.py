# Standard Library
import re
from collections import defaultdict, namedtuple
from collections.abc import Generator, Iterable
from itertools import product

# First Party
from utils import no_input_skip, read_input

Pattern = namedtuple("Pattern", ["id", "x", "y", "w", "h"])


def make_patterns(input: str) -> Iterable[Pattern]:
    regex = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    for line in input.splitlines():
        if (match := regex.search(line)) is not None:
            yield Pattern(*map(int, match.groups()))


def layout_patterns(patterns: Iterable[Pattern]) -> dict[tuple[int, int], int]:
    cloth = defaultdict(int)
    for _, x, y, w, h in patterns:
        for pos in product(range(x, x + w), range(y, y + h)):
            cloth[pos] += 1

    return cloth


def part_1(input: str) -> int:
    patterns = make_patterns(input)
    cloth = layout_patterns(patterns)
    return sum(1 for c in cloth.values() if c > 1)


def part_2(input: str) -> int:
    patterns = list(make_patterns(input))
    cloth = layout_patterns(patterns)

    def check_cloth(x, y, w, h) -> Generator[bool, None, None]:
        for pos in product(range(x, x + w), range(y, y + h)):
            yield cloth[pos] == 1

    for id, x, y, w, h in patterns:
        if all(check_cloth(x, y, w, h)):
            return id

    raise Exception("This should not happen")


# -- Tests


def get_example_input() -> str:
    return """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""


def test_part_1():
    test_input = get_example_input()
    assert part_1(test_input) == 4


def test_part_2():
    test_input = get_example_input()
    assert part_2(test_input) == 3


@no_input_skip
def test_part_1_real():
    real_input = read_input(__file__)
    assert part_1(real_input) == 112378


@no_input_skip
def test_part_2_real():
    real_input = read_input(__file__)
    assert part_2(real_input) == 603


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    part_2(get_example_input())
    # print(f"Part1: {part_1(real_input)}")
    # print(f"Part2: {part_2(real_input)}")
