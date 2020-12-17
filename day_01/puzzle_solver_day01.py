#!/usr/bin/env python3.7

"""Advent of Code 2020: Day 1"""

import itertools
import time

# loops

def puzzle_1_loops(expenses):
    for i in range(0, len(expenses)):
        for j in reversed(range(0, len(expenses))):
            expense_sum = expenses[i] + expenses[j]
            if expense_sum == 2020:
                expense_prod = expenses[i] * expenses[j]
                return (expenses[i], expenses[j]), expense_sum, expense_prod
    return ()

def puzzle_2_loops(expenses):
    for i in range(0, len(expenses)):
        for j in range(0, len(expenses)):
            if j == i:
                pass
            for k in range(0, len(expenses)):
                if k == i or k == j:
                    pass
                expense_sum = expenses[i] + expenses[j] + expenses[k]
                if expense_sum == 2020:
                    expense_prod = expenses[i] * expenses[j] * expenses[k]
                    return (expenses[i], expenses[j], expenses[k]), expense_sum, expense_prod
    return ()

# permutations

def puzzle_1_permutations(expenses):
    for expense_tuple in itertools.permutations(expenses, 2):
        expense_sum = sum(expense_tuple)
        if expense_sum == 2020:
            expense_prod = expense_tuple[0] * expense_tuple[1]
            return expense_tuple, expense_sum, expense_prod
    return ()

def puzzle_2_permutations(expenses):
    for expense_tuple in itertools.permutations(expenses, 3):
        expense_sum = sum(expense_tuple)
        if expense_sum == 2020:
            expense_prod = expense_tuple[0] * expense_tuple[1] * expense_tuple[2]
            return expense_tuple, expense_sum, expense_prod
    return ()

def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/10**6)

# Main
def main():
    with open("expenses.txt",  "r") as f:
        expenses = [int(expense) for expense in f.readlines()]
        expenses = sorted(expenses)

    print("Puzzle 1: find 2 expenses that sum to 2020")
    print(stopwatch(puzzle_1_loops, expenses))
    print(stopwatch(puzzle_1_permutations, expenses))

    print("\nPuzzle 2: find 3 expenses that sum to 2020")
    print(stopwatch(puzzle_2_loops, expenses))
    print(stopwatch(puzzle_2_permutations, expenses))

if __name__ == "__main__":
    main()
