#!/usr/bin/env python3.7

"""Advent of Code 2020: Day 1"""

import time

def slope_runner(landscape: list, step_x: int, step_y: int) -> int:
    y_max = len(landscape[0])
    tree_count = 0
    i = 0
    while (i * step_x) < len(landscape):
        tree_count += int(landscape[i * step_x][((i * step_y) % y_max)] == "#")
        i += 1
    return tree_count

def puzzle_1(landscape):
    return slope_runner(landscape, 1, 3)

def puzzle_2(landscape):
    result = 1
    for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        result *= slope_runner(landscape, slope[0], slope[1])
    return result

def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/10**6)

# Main
def main():
    with open("input.txt", "r") as f:
        landscape = [line.rstrip() for line in f.readlines()]

    print("-- Part One --")
    print(stopwatch(puzzle_1, landscape))

    print("\n-- Part Two --")
    print(stopwatch(puzzle_2, landscape))


if __name__ == "__main__":
    main()
