from util.helpy_functions import load_input


def parse_input():
    lines = load_input('./day04/input.txt')
    result = list()
    for line in lines:
        winning, numbers = [{int(v) for v in wn.split(' ') if len(v) > 0} for wn in
                            line.replace('\n', '').split(':')[1].split('|')]
        result.append((winning, numbers))
    return result


def task1():
    cards = parse_input()
    total = 0
    for idx, card in enumerate(cards):
        wins = card[0].intersection(card[1])
        if len(wins) > 0:
            points = (2 ** (len(wins) - 1))
            total += points
    return int(total)


def task2():
    cards = parse_input()
    cards_amount = [(card, 1) for card in cards]
    for idx in range(len(cards_amount)):
        card, amount = cards_amount[idx]
        wins = len(card[0].intersection(card[1]))
        for offset in range(1, wins + 1):
            c_, a_ = cards_amount[idx + offset]
            cards_amount[idx + offset] = (c_, a_ + amount)
    return sum([v[1] for v in cards_amount])
