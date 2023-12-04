# Standard Library

# First Party
from utils import no_input_skip, read_input


def part_1(input: str) -> int:
    polymer = []

    for unit in [ord(i) for i in input]:
        if polymer and abs(unit - polymer[-1]) == 32:
            polymer.pop()
        else:
            polymer.append(unit)

    return len(polymer)


def part_2(input: str) -> int:
    units = [str.maketrans({c.lower(): "", c.upper(): ""}) for c in set(input)]
    return min([part_1(input.translate(trans)) for trans in units])


# -- Tests


def get_example_input() -> str:
    return """dabAcCaCBAcCcaDA"""


def test_part_1():
    test_input = get_example_input()
    assert part_1(test_input) == 10


def test_part_2():
    test_input = get_example_input()
    assert part_2(test_input) == 4


@no_input_skip
def test_part_1_real():
    real_input = read_input(__file__)
    assert part_1(real_input) == 9900


@no_input_skip
def test_part_2_real():
    real_input = read_input(__file__)
    assert part_2(real_input) == 4992


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
