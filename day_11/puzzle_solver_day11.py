#!/usr/bin/env python3.7
import time

def count_occupied(x: int, y: int, seats: list, consider_floor_empty=True) -> int:
    directions = dict()
    offset = 0
    while len(list(directions)) != 8:
        offset += 1
        for i in [-offset, 0, offset]:
            for j in [-offset, 0, offset]:
                if (i/offset, j/offset) in list(directions): continue
                if i == 0 and j == 0: continue
                if not (y + j) in range(0, len(seats)) or not (x + i) in range(0, len(seats[0])):
                    directions[(i/offset, j/offset)] = 'empty'
                elif seats[y+j][x+i] == '#':
                    directions[(i/offset, j/offset)] = 'occupied'
                elif seats[y+j][x+i] == 'L':
                    directions[(i/offset, j/offset)] = 'empty'
                elif seats[y+j][x+i] == '.' and consider_floor_empty:
                    directions[(i/offset, j/offset)] = 'empty'
                else:
                    continue
    return len([_ for _ in list(directions) if directions[_] == 'occupied'])

def update_seats(seats: list, tolerance:int, consider_floor_empty: bool) -> list:
    seats_update = list()
    for y in range(len(seats)):
        row = seats[y].copy()
        for x in range(len(seats[0])):
            if seats[y][x] == 'L' and count_occupied(x, y, seats, consider_floor_empty) == 0:
                row[x] = '#'
            elif seats[y][x] == '#' and count_occupied(x, y, seats, consider_floor_empty) >= tolerance:
                row[x] = 'L'
            else:
                continue
        seats_update.append(row)
    return seats_update

def stringify(seats: list) -> str:
    return (''.join(map(str, ["".join(map(str, _)) for _ in seats])))

def seat_loop(seats: list, tolerance:int, consider_floor_empty: bool) -> int:
    seats_update = update_seats(seats, tolerance, consider_floor_empty)
    while stringify(seats) != stringify(seats_update):
        seats = seats_update
        seats_update = update_seats(seats, tolerance, consider_floor_empty)
    return len([_ for _  in stringify(seats_update) if _ == '#'])


def part_1(input: list) -> int:
    return seat_loop(input, 4, consider_floor_empty=True)

def part_2(input: list) -> int:
    return seat_loop(input, 5, consider_floor_empty=False)

def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/10**6)

# Main
def main():
    with open("input", "r") as f:
        input = [list(_) for _ in f.read().split("\n")]

    print("-- Part One --")
    print(stopwatch(part_1, input))

    print("\n-- Part Two --")
    print(stopwatch(part_2, input))


if __name__ == "__main__":
    main()
