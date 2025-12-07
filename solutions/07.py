from collections import defaultdict

from utils.runtime import get_runtime


def get_input(test: str = None):
    if test is not None:
        base = test
    else:
        with open("inputs/07") as f:
            base = f.read()
    result = []
    for line in base.splitlines():
        if line == "":
            continue
        result.append([l for l in line])
    return result


def index_all(input_list: list[str], target_char: str) -> list[int]:
    indices = [i for i, v in enumerate(input_list) if v == target_char]
    return indices


@get_runtime
def part_1(l: list[list[str]]):
    split_count = 0
    rows = []
    starter = l[0]
    starter_pos = starter.index("S")
    rows.append(starter)
    current_beam_pos = [starter_pos]
    l = l[1:]
    for i in l:
        next_positions_map = {}
        for pos in current_beam_pos:
            if pos < 0 or pos >= len(i):
                continue

            char = i[pos]
            if char == "^":
                split_count += 1
                next_positions_map[pos - 1] = True
                next_positions_map[pos + 1] = True
            else:
                next_positions_map[pos] = True
                i[pos] = "|"
        current_beam_pos.clear()
        for k in next_positions_map:
            current_beam_pos.append(k)
    print(split_count)


@get_runtime
def part_2(l: list[list[str]]):
    starter = l[0]
    try:
        starter_pos = starter.index("S")
    except ValueError:
        print("Start position 'S' not found.")
        return

    current_timelines = defaultdict(int)
    current_timelines[starter_pos] = 1

    grid = l[1:]
    if not grid:
        print(0)
        return

    width = len(grid[0])

    for row in grid:
        next_timelines = defaultdict(int)

        for pos, count in current_timelines.items():
            if pos < 0 or pos >= width:
                continue

            char = row[pos]

            if char == "^":
                if pos - 1 >= 0:
                    next_timelines[pos - 1] += count
                if pos + 1 < width:
                    next_timelines[pos + 1] += count
            else:
                next_timelines[pos] += count

        current_timelines = next_timelines

    total_timelines = sum(current_timelines.values())
    print(total_timelines)
    return total_timelines


test_input = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


# part_1(get_input(test=test_input))
part_1(get_input())
# part_2(get_input(test=test_input))
part_2(get_input())
