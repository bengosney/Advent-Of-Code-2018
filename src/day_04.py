# Standard Library
import re
from collections import defaultdict
from typing import Any, TypeVar

# First Party
from utils import no_input_skip, read_input


def get_min(line) -> int:
    if (match := re.search(r":(\d+)", line)) is None:
        raise Exception("Min not found")
    return int(match.group(1))


def get_guard(line) -> int:
    if (match := re.search(r"#(\d+)", line)) is None:
        raise Exception("Guard not found")
    return int(match.group(1))


T = TypeVar("T")


def best(items: dict[T, Any]) -> T:
    return max(items, key=lambda i: items.get(i, None))


def get_counts(lines: list[str]):
    shift_counts: dict[int, int] = defaultdict(int)
    minute_counts: dict[tuple[int, int], int] = defaultdict(int)
    current_guard = -1
    sleep_start = -1

    for line in lines:
        if "begins shift" in line:
            current_guard = get_guard(line)
            sleep_start = -1
        if "falls asleep" in line:
            sleep_start = get_min(line)
        if "wakes up" in line:
            if current_guard == -1 or sleep_start == -1:
                raise Exception(f"Invalid data: current_guard - {current_guard}, sleep_start - {sleep_start} ")
            for min in range(sleep_start, get_min(line)):
                shift_counts[current_guard] += 1
                minute_counts[(current_guard, min)] += 1

    return shift_counts, minute_counts


def part_1(input: str) -> int:
    shift_counts, minute_counts = get_counts(sorted(input.splitlines()))

    best_guard = best(shift_counts)
    best_minute = best({m: v for (g, m), v in minute_counts.items() if g == best_guard})

    return best_guard * best_minute


def part_2(input: str) -> int:
    _, minute_counts = get_counts(sorted(input.splitlines()))

    idx, minute = best(minute_counts)
    return idx * minute


# -- Tests


def get_example_input() -> str:
    return """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""


def test_part_1():
    test_input = get_example_input()
    assert part_1(test_input) == 240


def test_part_2():
    test_input = get_example_input()
    assert part_2(test_input) == 4455


@no_input_skip
def test_part_1_real():
    real_input = read_input(__file__)
    assert part_1(real_input) == 21956


@no_input_skip
def test_part_2_real():
    real_input = read_input(__file__)
    assert part_2(real_input) == 134511


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
