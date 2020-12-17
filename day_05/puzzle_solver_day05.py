#!/usr/bin/env python3.7

import time

def get_seat_id(seat: str) -> int:
    return (
        int('0b{}{}'.format(
            seat[:7].replace('F', '0').replace('B', '1'),
            seat[7:].replace('L', '0').replace('R', '1')
            ), base=2)
    )

def free_seat(seats: list) -> int:
    seats = sorted([get_seat_id(seat) for seat in seats])
    for seat_id in range(seats[0], seats[-1]):
        if seats[seat_id] + 2 == seats[seat_id + 1]:
            return seats[seat_id] + 1


def part_1(seats: list) -> int:
    return max([get_seat_id(seat) for seat in seats])

def part_2(seats: list) -> int:
    return free_seat(seats)

def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/10**6)

# Main
def main():
    with open("input", "r") as f:
        seats = f.read().split("\n")

    print("-- Part One --")
    print(stopwatch(part_1, seats))

    print("\n-- Part Two --")
    print(stopwatch(part_2, seats))


if __name__ == "__main__":
    main()
