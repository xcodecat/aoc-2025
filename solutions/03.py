from utils.runtime import get_runtime


def get_input(test: str = None):
    if test is not None:
        base = test
    else:
        with open("inputs/03") as f:
            base = f.read()
    return [line.strip() for line in base.splitlines() if line.strip()]


@get_runtime
def part_1(l: list[str]):
    total = 0
    for bank in l:
        max_joltage = -1
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                d1 = ord(bank[i]) - ord("0")
                d2 = ord(bank[j]) - ord("0")
                current_joltage = (d1 * 10) + d2
                if current_joltage > max_joltage:
                    max_joltage = current_joltage
        total += max_joltage
    print(total)
    return total


def part_2(data):
    total = 0
    target_length = 12
    for bank in data:
        if len(bank) < target_length:
            continue
        current_pos = 0
        needed = target_length
        sb = []
        while needed > 0:
            search_end = len(bank) - needed
            best_digit = -1
            best_index = -1
            for i in range(current_pos, search_end + 1):
                digit = ord(bank[i]) - ord("0")
                if digit > best_digit:
                    best_digit = digit
                    best_index = i

            sb.append(str(best_digit))
            current_pos = best_index + 1
            needed -= 1

        val = int("".join(sb))
        total += val
    print(total)
    return total


test_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

print("Test Part1:", part_1(get_input(test_input)))
print("Real Part1:", part_1(get_input()))
print("Test Part2:", part_2(get_input(test_input)))
print("Real Part2:", part_2(get_input()))
