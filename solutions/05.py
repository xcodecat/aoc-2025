from utils.runtime import get_runtime


def get_input(test: str = None):
    if test is not None:
        base = test
    else:
        with open("inputs/05") as f:
            base = f.read()
    return base.splitlines()


@get_runtime
def part_1(l: list[str]):
    ranges = []
    ingredients = []
    count = 0
    for line in l:
        if line == "":
            continue
        elif "-" in line:
            splitted = line.split("-")
            ranges.append(splitted)
        else:
            ingredients.append(int(line))
    ranges = merge_ranges(ranges)
    for ingredient in ingredients:
        for range in ranges:
            if ingredient >= int(range[0]) and ingredient <= int(range[1]):
                count += 1
                break
    print(count)


def merge_ranges(l: list[list[str]]):
    l_sorted = sorted(l, key=lambda x: int(x[0]))

    merged = []

    for element in l_sorted:
        start = int(element[0])
        end = int(element[1])
        if len(merged) == 0 or start > merged[-1][1] + 1:
            merged.append([start, end])
        elif end > merged[-1][1]:
            merged[-1][1] = end

    return merged


@get_runtime
def part_2(l: list[str]):
    ranges = []
    count = 0
    for line in l:
        if line == "":
            continue
        elif "-" in line:
            splitted = line.split("-")
            ranges.append(splitted)
    ranges = merge_ranges(ranges)
    for r in ranges:
        count += len(range(int(r[0]), int(r[1]))) + 1
    print(count)


test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

# part_1(get_input(test=test_input))
part_1(get_input())
# part_2(get_input(test=test_input))
part_2(get_input())
