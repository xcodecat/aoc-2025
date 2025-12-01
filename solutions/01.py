from utils.runtime import get_runtime


def get_input(test: str = None):
    with open("inputs/01") as f:
        base = test or f.read()
        l = base.splitlines()

    return l


@get_runtime
def part_1(l: list[str]):
    pos = 50
    count = 0
    for line in l:
        direction = line[0]
        steps = int(line[1:])
        if direction == "R":
            pos = (pos + steps) % 100
        elif direction == "L":
            pos = (pos - steps) % 100
        elif pos == 0:
            count += 1
    print(count)
    return count


@get_runtime
def part_2(l: list[str]):
    pos = 50
    count = 0
    for line in l:
        direction = line[0]
        steps = int(line[1:])
        if direction == "R":
            for _ in range(steps):
                pos = (pos + 1) % 100
                if pos == 0:
                    count += 1
        elif direction == "L":
            for _ in range(steps):
                pos = (pos - 1) % 100
                if pos == 0:
                    count += 1
    print(count)
    return count


part_1(get_input())
part_2(get_input())
