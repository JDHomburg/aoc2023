from util.helpy_functions import load_input
import math


def parse_input(file_name):
    input_txt = load_input(file_name)
    result = dict()
    for line in input_txt:
        game, samples = line.split(': ')
        repeats = samples.split('; ')
        repeats = [{value_color.split(' ')[1].replace('\n', ''): int(value_color.split(' ')[0]) for value_color in
                    sample.split(', ')} for sample in repeats]
        game = game.split(' ')[1]
        result[game] = repeats
    return result


def task1(file_name='./day02/input_task1.txt'):
    parsed_input = parse_input(file_name)
    value = 0
    max_values = {'red': 12,
                  'green': 13,
                  'blue': 14}
    for game, samples in parsed_input.items():
        if all([max_values[color] >= value for sample in samples for color, value in sample.items()]):
            value += int(game)
    return value


def task2(file_name='./day02/input_task1.txt'):
    parsed_input = parse_input(file_name)
    value = 0
    for game, samples in parsed_input.items():
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for sample in samples:
            for color, cubes in sample.items():
                min_cubes[color] = max(min_cubes[color], cubes)
        value += math.prod([v for v in min_cubes.values() if v > 0])
    return value


if __name__ == '__main__':
    print(task1())
