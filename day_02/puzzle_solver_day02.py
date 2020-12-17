#!/usr/bin/env python3.7

"""Advent of Code 2020: Day 1"""

import time

def rule_match_cnt(rule: str, password: str) -> bool:
    char = str(rule.split(' ')[1])
    min_cnt = int(rule.split(' ')[0].split('-')[0])
    max_cnt = int(rule.split(' ')[0].split('-')[1])
    if (password.count(char) > max_cnt) or (password.count(char) < min_cnt):
        return False
    return True

def rule_match_pos(rule: str, password: str) -> bool:
    char = str(rule.split(' ')[1])
    pos_1 = int(rule.split(' ')[0].split('-')[0]) - 1
    pos_2 = int(rule.split(' ')[0].split('-')[1]) - 1
    if (password[pos_1] == char) ^ (password[pos_2] == char):
        return True
    return False

def puzzle_1(passwords):
    return len([password[1] for password in passwords if rule_match_cnt(password[0], password[1])])

def puzzle_2(passwords):
    return len([password[1] for password in passwords if rule_match_pos(password[0], password[1])])


def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/10**6)

# Main
def main():
    with open("passwords.txt",  "r") as f:
        passwords = [line.rstrip().split(":") for line in f.readlines()]
        passwords = [[password[0], password[1].lstrip()] for password in passwords]

    print("Puzzle 1: Password count matching the rule count.")
    print(stopwatch(puzzle_1, passwords))

    print("\nPuzzle 2: Password count matching the rule pos.")
    print(stopwatch(puzzle_2, passwords))


if __name__ == "__main__":
    main()
