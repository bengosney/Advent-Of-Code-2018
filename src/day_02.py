# Standard Library
from collections import Counter
from itertools import combinations

# First Party
from utils import no_input_skip, read_input


def part_1(input: str) -> int:
    counter: Counter = Counter()
    for line in input.splitlines():
        counter.update({count for _, count in Counter(line).most_common()})
    counts = dict(counter.most_common())
    return counts[2] * counts[3]


def part_2(input: str) -> str:
    for a, b in combinations(input.splitlines(), 2):
        overlap = [c for i, c in enumerate(a) if c == b[i]]
        if len(overlap) == len(a) - 1:
            return "".join(overlap)
    raise Exception("This can not happen")


# -- Tests


def get_example_input_1() -> str:
    return """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""


def test_part_1():
    test_input = get_example_input_1()
    assert part_1(test_input) == 12


def get_example_input_2() -> str:
    return """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""


def test_part_2():
    test_input = get_example_input_2()
    assert part_2(test_input) == "fgij"


@no_input_skip
def test_part_1_real():
    real_input = read_input(__file__)
    assert part_1(real_input) == 6150


@no_input_skip
def test_part_2_real():
    real_input = read_input(__file__)
    assert part_2(real_input) == "rteotyxzbodglnpkudawhijsc"


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
