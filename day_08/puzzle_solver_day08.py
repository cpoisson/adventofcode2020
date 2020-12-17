#!/usr/bin/env python3.7

import time

class ProgramState(object):

    def __init__(self):
        self.accumulator = 0
        self.address = 0
        self.callstack = []
        self.error = ''

    def __repr__(self) -> str:
        return f'<acc: {self.accumulator}, addr: {self.address}, stack: {self.callstack}, err: {self.error}>'

def run_program(instructions: list) -> ProgramState:
    state = ProgramState()
    while state.address in range(len(instructions)):
        if state.address in state.callstack:
            state.error = 'infinite loop detected at ${}'.format(state.address)
            break

        state.callstack.append(state.address)

        instruction = instructions[state.address].split(" ")
        if instruction[0] == 'nop':
            state.address += 1
        if instruction[0] == "jmp":
            state.address += int(instruction[1])
        if instruction[0] == "acc":
            state.accumulator += int(instruction[1])
            state.address += 1

    return state

def fix_program(instructions: list) -> ProgramState:

    crash_state = run_program(instructions)

    for address in reversed(crash_state.callstack):

        fixed_instructions = instructions.copy()

        if instructions[address].split(' ')[0] == 'nop':
            fixed_instructions[address] = fixed_instructions[address].replace('nop', 'jmp')
        elif instructions[address].split(' ')[0] == 'jmp':
            fixed_instructions[address] = fixed_instructions[address].replace('jmp', 'nop')
        else:
            continue

        program_state = run_program(fixed_instructions)

        if program_state.error:
            continue

        return program_state


def part_1(input: list) -> int:
    return run_program(input).accumulator

def part_2(input: list) -> int:
    return fix_program(input).accumulator


def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/1000)

# Main
def main():
    with open("input", "r") as f:
        input = f.read().split("\n")

    print("-- Part One --")
    print(stopwatch(part_1, input))

    print("\n-- Part Two --")
    print(stopwatch(part_2, input))


if __name__ == "__main__":
    main()
