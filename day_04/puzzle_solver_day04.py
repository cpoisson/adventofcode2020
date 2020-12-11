#!/usr/bin/env python3.7

import time

def valid_digit(value: str, lenght: int, val_min: int, val_max: int) -> bool:
    if value.isalpha(): return False
    if len(value) != lenght: return False
    if int(value) < val_min or int(value) > val_max: return False
    return True

def valid_height(value: str) -> bool:
    if value[-2:] not in ['cm', 'in'] or value[:-2].isalpha():
        return False
    if value[-2:] == 'cm' and (int(value[:-2]) < 150 or int(value[:-2]) > 193):
        return False
    if value[-2:] == 'in' and (int(value[:-2]) < 59 or int(value[:-2]) > 76):
        return False
    return True

def valid_hair_color(value: str) -> bool:
    if value[0] != '#' or len(value) != 7: return False
    try:
        int(value[1:], 16)
    except ValueError:
        return False
    return True

def valid_eye_color(value:str) -> bool:
    return (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def field_is_valid(string: str, field: str) -> bool:
    value = string.replace('\n', ' ').split("{}:".format(field))[1].split(' ')[0]
    if field == 'byr': return valid_digit(value, 4, 1920, 2002)
    if field == 'iyr': return valid_digit(value, 4, 2010, 2020)
    if field == 'eyr': return valid_digit(value, 4, 2020, 2030)
    if field == 'hgt': return valid_height(value)
    if field == 'hcl': return valid_hair_color(value)
    if field == 'ecl': return valid_eye_color(value)
    if field == 'pid': return valid_digit(value, 9, 0, int('9'* 9))
    return False

def contains_fields(string: str, fields: list, data_valid: bool) -> bool:
    for field in fields:
        if field not in string:
            return False
        if data_valid and (not field_is_valid(string, field)):
            return False
    return True

def filter_valid_passports(passports: list, data_valid: bool):
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return [
        passport for passport in passports
        if contains_fields(passport, mandatory_fields, data_valid)
        ]

def part_1(passports: list) -> int:
    return len(filter_valid_passports(passports, data_valid=False))

def part_2(passports: list) -> int:
    return len(filter_valid_passports(passports, data_valid=True))

def stopwatch(func, arg):
    t_start = time.process_time_ns()
    result = func(arg)
    t_elapsed = time.process_time_ns() - t_start
    return "⚙️ {} -> {} -> ⏱️ {} ms".format(func.__name__, result, t_elapsed/1000)

# Main
def main():
    with open("input", "r") as f:
        passports = f.read().split("\n\n")

    print("-- Part One --")
    print(stopwatch(part_1, passports))

    print("\n-- Part Two --")
    print(stopwatch(part_2, passports))


if __name__ == "__main__":
    main()
