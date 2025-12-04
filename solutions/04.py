from utils.runtime import get_runtime


def get_input(test: str = None):
    if test is not None:
        base = test
    else:
        with open("inputs/04") as f:
            base = f.read()
    return base.splitlines()


DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def parse_grid(text_data):
    grid = []
    for line in text_data.splitlines():
        if not line.strip():
            continue
        char_list = list(line)
        grid.append(char_list)

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    return grid, rows, cols


def count_neighbors(grid, x, y, rows, cols):
    count = 0
    for dx, dy in DIRECTIONS:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < cols and 0 <= ny < rows:
            if grid[ny][nx] == "@":
                count += 1
    return count


@get_runtime
def part_1(lines: list[str]):
    data = "\n".join(lines)
    grid, rows, cols = parse_grid(data)
    accessible_count = 0

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] != "@":
                continue
            neighbors = count_neighbors(grid, x, y, rows, cols)
            if neighbors < 4:
                accessible_count += 1

    return accessible_count


@get_runtime
def part_2(lines: list[str]):
    data = "\n".join(lines)
    grid, rows, cols = parse_grid(data)
    total_removed = 0

    while True:
        to_remove = []
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == "@":
                    neighbors = count_neighbors(grid, x, y, rows, cols)
                    if neighbors < 4:
                        to_remove.append((x, y))

        if not to_remove:
            break

        total_removed += len(to_remove)
        for x, y in to_remove:
            grid[y][x] = "."

    return total_removed


test_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

print("Test Part1:", part_1(get_input(test_input)))
print("Real Part1:", part_1(get_input()))
print("Test Part2:", part_2(get_input(test_input)))
print("Real Part2:", part_2(get_input()))
