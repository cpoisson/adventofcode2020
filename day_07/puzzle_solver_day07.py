#!/usr/bin/env python3.7

import time

def ancestors_look_up(root_node: str, vertices: list) -> list:
    ancestors = list()
    parents = [vertex[0] for vertex in vertices if vertex[1] == root_node]
    for node in parents:
        vertices = [vertex for vertex in vertices if vertex[0] not in [node, root_node]]
        ancestors += ancestors_look_up(node, vertices)
    return set(parents + ancestors)

def get_child_count(root_node:str, vertices: list) -> list:
    childs = [vertex for vertex in vertices if vertex[0] == root_node]
    child_count = 0
    for vertex in childs:
        child_count += (get_child_count(vertex[1], vertices) + 1) * vertex[2]
    return child_count

def part_1(input: list) -> int:
    authorized_colors = ancestors_look_up('shiny gold', input)
    return len(authorized_colors)

def part_2(input: list) -> int:
    return get_child_count('shiny gold', input)

def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/1000)

# Main
def main():
    with open("input", "r") as f:
        input = list()
        for _ in f.read().split("\n"):
            _ = _[:-1].replace(' bags', '').replace(' bag', '').split(' contain ')
            for __ in _[1].split(', '):
                if __ != 'no other':
                    input.append(
                       (_[0], '{} {}'.format(__.split(' ')[1], __.split(' ')[2]), int(__.split(' ')[0]))
                    )

    print("-- Part One --")
    print(stopwatch(part_1, input))

    print("\n-- Part Two --")
    print(stopwatch(part_2, input))


if __name__ == "__main__":
    main()
