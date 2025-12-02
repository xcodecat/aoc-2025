from utils.runtime import get_runtime


def get_input(test: str = None):
    if test is not None:
        base = test
    else:
        with open("inputs/02") as f:
            base = f.read()
    l = base.splitlines()
    return l


def is_invalid_part1(num: int) -> bool:
    s = str(num)
    n = len(s)
    if n % 2 == 0:
        half = n // 2
        return s[:half] == s[half:]
    return False


def is_invalid_part2(num: int) -> bool:
    s = str(num)
    n = len(s)
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            segment = s[:length]
            repeats = n // length
            if repeats >= 2 and segment * repeats == s:
                if not (length > 1 and segment.startswith("0")):
                    return True
    return False


@get_runtime
def part_1(lines: list[str]):
    total_sum = 0
    for line in lines:
        ranges = line.split(",")
        for r in ranges:
            if not r.strip():
                continue
            start, end = map(int, r.split("-"))
            for num in range(start, end + 1):
                if is_invalid_part1(num):
                    total_sum += num
    print(f"Part 1: {total_sum}")


@get_runtime
def part_2(l: list[str]):
    total_sum = 0
    for line in l:
        ranges = line.split(",")
        for r in ranges:
            if not r.strip():
                continue
            start, end = map(int, r.split("-"))
            for num in range(start, end + 1):
                if is_invalid_part2(num):
                    total_sum += num
    print(f"Part 2: {total_sum}")


test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
part_1(get_input(test=test_input))
part_1(get_input())
part_2(get_input(test=test_input))
part_2(get_input())
