#!/usr/bin/env python3.7

import time
from collections import namedtuple

class Edge(object):
    def __init__(self, target: str, origin: str, weight: int):
        self.target = target
        self.origin = origin
        self.weight = weight

    def __hash__(self) -> int:
        return hash('{}{}{}'.format(self.target, self.origin, self.weight))

    def __repr__(self) -> str:
        return "<{}, {}, {}>".format(self.target, self.origin, self.weight)

def successors_look_up(origin: str, edges: list) -> list:
    successors = list()
    direct_successors = [edge.target for edge in edges if edge.origin == origin]
    for node in direct_successors:
        edges = [edge for edge in edges if edge.target not in [node, origin]]
        successors += successors_look_up(node, edges)
    return set(direct_successors + successors)

def get_successors(origin:str, edges: set) -> set: # does not work, needs debug
    direct_successors = set([edge for edge in edges if edge.origin == origin])
    successors = set()
    for edge in direct_successors:
        successors |= set([edge])
        successors |= get_successors(edge.target, edges)
    return successors

def predecessor_weighted_count(target:str, edges: list) -> list:
    predecessors = [edge for edge in edges if edge.target == target]
    count = 0
    for edge in predecessors:
        count += (predecessor_weighted_count(edge.origin, edges) + 1) * edge.weight
    return count

def part_1(input: list) -> int:
    return len(successors_look_up('shiny gold', input))
    #return len(get_successors('shiny gold', set(input)))

def part_2(input: list) -> int:
    return predecessor_weighted_count('shiny gold', input)

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
                        Edge(
                           _[0],
                           '{} {}'.format(__.split(' ')[1], __.split(' ')[2]),
                           int(__.split(' ')[0])
                        )
                    )

    print("-- Part One --") # 287
    print(stopwatch(part_1, input))

    print("\n-- Part Two --") # 48160
    print(stopwatch(part_2, input))


if __name__ == "__main__":
    main()
