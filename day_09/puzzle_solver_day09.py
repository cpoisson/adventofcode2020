#!/usr/bin/env python3.7

import time
from itertools import combinations

def find_invalid_numbers(input:list) -> list:
    return [
        input[i] for i in range(25, len(input))
        if not [_ for _ in combinations(input[i-25:i], 2) if sum(_) == input[i]]
    ]

def find_contiguous_sum(input: list, criteria: int) -> list:
    for bin_size in range(2, int(len(input)/2)):
        for i in range(len(input)-bin_size):
            contiguous = input[i:i+bin_size]
            if sum(contiguous) == criteria:
                return input[i:i+bin_size]
    return []


def part_1(input: list) -> int:
    return find_invalid_numbers(input)[0]

def part_2(input: list) -> int:
    result = find_contiguous_sum(input, find_invalid_numbers(input)[0])
    return min(result) + max(result)


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
