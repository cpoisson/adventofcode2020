#!/usr/bin/env python3.7

import time

def chain_adaptors(input: list) -> list:
    return sorted(input + [0, max(input) + 3])

def get_jolt_differences(chained_adaptors: list) -> list:
    return [(chained_adaptors[i] - chained_adaptors[i - 1]) for i in range(1, len(chained_adaptors))]

def arrangements(lenght: int) -> int:
    if lenght <= 1:
        return 1
    elif lenght == 2:
        return 2
    elif lenght == 3:
        return 4
    else:
        return (1 + 2*(arrangements(lenght - 1)  - 1))

def find_arrangements(chained_adaptors: list) -> int:
    """Find all the chains of '1's separated by a '3' where arrangements are possible."""

    differences = get_jolt_differences(chained_adaptors)
    total_arrangements = 1
    for _  in ''.join(map(str, differences)).split('3'):
        total_arrangements *= arrangements(len(_))
    return total_arrangements


def part_1(input: list) -> int:
    differences = get_jolt_differences(chain_adaptors(input))
    return len([_ for _ in differences if _ == 1]) *  len([_ for _ in differences if _ == 3])

def part_2(input: list) -> int:
    return find_arrangements(chain_adaptors(input))


def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/10**6)

# Main
def main():
    with open("input", "r") as f:
        input = [int(_) for _ in f.read().split("\n")]

    print("-- Part One --")
    print(stopwatch(part_1, input))

    print("\n-- Part Two --")
    print(stopwatch(part_2, input))


if __name__ == "__main__":
    main()
