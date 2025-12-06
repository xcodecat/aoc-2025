from utils.runtime import get_runtime


def get_input(test: str = None):
    if test is not None:
        base = test
    else:
        with open("inputs/06") as f:
            base = f.read()
    result = []
    for line in base.splitlines():
        if line == "":
            continue
        result.append([l for l in line.split() if len(l) > 0])
    # print(result)
    return result


def get_input2(test: str = None):
    if test is not None:
        base = test
    else:
        with open("inputs/06") as f:
            base = f.read()
    result = []
    for line in base.splitlines():
        if line == "":
            continue
        result.append([l for l in line])
    # print(result)
    return result


@get_runtime
def part_1(l: list[list[str]]):
    total = 0
    for col in range(len(l[0])):
        numbers = []
        op = ""
        for row in range(len(l) - 1):
            val = l[row][col]
            if val.isdigit():
                numbers.append(int(val))
        op = l[-1][col]
        if op == "*":
            result = 1
        else:
            result = 0
        for n in numbers:
            if op == "*":
                result *= n
            else:
                result += n
        total += result
    print(total)


@get_runtime
def part_2(l: list[list[str]]):
    max_width = max(len(row) for row in l)
    grid = [row + [" "] * (max_width - len(row)) for row in l]
    cols = list(zip(*grid))

    grand_total = 0
    current_numbers = []
    current_op = None

    for x in range(len(cols) - 1, -1, -1):
        col = cols[x]
        is_separator = all(c == " " for c in col)

        digits = [c for c in col if c.isdigit()]
        if digits:
            number = int("".join(digits))
            current_numbers.append(number)

        for c in col:
            if c in ("+", "*"):
                current_op = c

        if is_separator or x == 0:
            if current_numbers and current_op:
                block_res = current_numbers[0]
                for n in current_numbers[1:]:
                    if current_op == "+":
                        block_res += n
                    elif current_op == "*":
                        block_res *= n
                grand_total += block_res

            current_numbers = []
            current_op = None

    print(grand_total)


test_input = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""

# part_1(get_input(test=test_input))
part_1(get_input())
# part_2(get_input2(test=test_input))
part_2(get_input2())
