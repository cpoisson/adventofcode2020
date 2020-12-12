#!/usr/bin/env python3.7

import time

def count_yes_union(group_answers: list) -> int:
    answer_union = set()
    for answer in group_answers:
        answer_union |= answer
    return len(answer_union)

def count_yes_intersection(group_answers: list) -> int:
    answer_intersection = group_answers[0]
    for answer in group_answers:
        answer_intersection &= answer
    return len(answer_intersection)

def part_1(input: list) -> int:
    return sum(map(count_yes_union, input))

def part_2(input: list) -> int:
    return sum(map(count_yes_intersection, input))

def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/1000)

# Main
def main():
    with open("input", "r") as f:
        input = [[set(__) for (__) in _.split("\n")] for _ in f.read().split("\n\n")]

    print("-- Part One --")
    print(stopwatch(part_1, input))

    print("\n-- Part Two --")
    print(stopwatch(part_2, input))


if __name__ == "__main__":
    main()
