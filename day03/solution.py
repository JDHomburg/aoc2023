import math
import re

from util.helpy_functions import load_input


def parse_input(file_name='./day03/input.txt'):
    input_text = load_input(file_name)
    number_map = dict()
    for y, line in enumerate(input_text):
        for m in re.finditer('\d+', line):
            for x in range(m.start(), m.end()):
                number_map[(y, x)] = m
    return number_map, input_text


def task1():
    numbers, input_text = parse_input()
    result = dict()
    for y, line in enumerate(input_text):
        for symbol in re.finditer('[^\d\.\n]', line):
            for y_ in range(y - 1, y + 2):
                for x_ in range(symbol.start() - 1, symbol.start() + 2):
                    value = numbers.get((y_, x_), 0)
                    if value != 0:
                        result[id(value)] = int(value.group())
    return sum(result.values())


def task2():
    numbers, input_text = parse_input()
    result = 0
    for y, line in enumerate(input_text):
        for symbol in re.finditer('[^\d\.\n]', line):
            if symbol.group() != '*':
                continue
            tmp = dict()
            for y_ in range(y - 1, y + 2):
                for x_ in range(symbol.start() - 1, symbol.start() + 2):
                    value = numbers.get((y_, x_), 0)
                    if value != 0:
                        tmp[id(value)] = int(value.group())
            if len(tmp) != 2:
                continue
            result += math.prod(tmp.values())
    return result
