import re


def task1(file_name='./input_task1.txt'):
    value = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            first = re.search('\d', line)
            last = re.search('\d', line[::-1])
            tmp = int(first.group() + last.group())
            value += tmp
    return value


def task2(file_name='./input_task1.txt'):
    value_map = {'zero': '0',
                 'one': '1',
                 'two': '2',
                 'three': '3',
                 'four': '4',
                 'five': '5',
                 'six': '6',
                 'seven': '7',
                 'eight': '8',
                 'nine': '9'}
    for i in range(10):
        value_map[str(i)] = str(i)
    value = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            findings = re.finditer(r'(?=((\d|zero|one|two|three|four|five|six|seven|eight|nine)))', line)
            finding = [match.group(1) for match in findings]
            tmp = int(value_map[finding[0]] + value_map[finding[-1]])
            value += tmp
    return value


if __name__ == '__main__':
    print(task1())
    print(task2('./input_task1.txt'))
