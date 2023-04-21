def task2():
    data = open('task2.txt', 'r').read().split('\n')
    ROCK, PAPER, SCISSOR = 1,2,3
    options = {"A": ROCK, "B": PAPER, "C": SCISSOR, "X": ROCK, "Y": PAPER, "Z": SCISSOR}
    interactions = {f'{ROCK},{ROCK}': 3, f'{ROCK},{PAPER}': 0, f'{ROCK},{SCISSOR}': 6,
                    f'{PAPER},{PAPER}': 3, f'{PAPER},{SCISSOR}': 0, f'{PAPER},{ROCK}': 6,
                    f'{SCISSOR},{SCISSOR}': 3, f'{SCISSOR},{ROCK}': 0, f'{SCISSOR},{PAPER}': 6}
    res = 0
    for round in data:
        res += options[round[-1]]
        res += interactions[f'{options[round[-1]]},{options[round[0]]}']
    return res

def part2():
    data = open('task2.txt', 'r').read().split('\n')
    ROCK, PAPER, SCISSOR = 1, 2, 3
    options = {"A": ROCK, "B": PAPER, "C": SCISSOR}
    interactions = {f'{ROCK},X': SCISSOR, f'{ROCK},Y': ROCK+3, f'{ROCK},Z': PAPER+6,
                    f'{PAPER},X': ROCK, f'{PAPER},Y': PAPER+3, f'{PAPER},Z': SCISSOR+6,
                    f'{SCISSOR},X': PAPER, f'{SCISSOR},Y': SCISSOR+3, f'{SCISSOR},Z': ROCK+6}
    res = 0
    for round in data:
        res+= interactions[f'{options[round[0]]},{round[-1]}']
    return res


if __name__ == '__main__':
    print(task2())
    print(part2())