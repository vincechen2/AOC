def task4():
    data = open('task4.txt', 'r').read().split('\n')
    res = 0
    for s in data:
        s = s.split(',')
        s[0], s[1] = list(map(int,s[0].split('-'))),list(map(int,s[1].split('-')))
        s.sort(key = lambda x : (x[0], -x[1]))
        s1, e1, s2, e2 = s[0][0], s[0][-1], s[1][0], s[1][-1]

        if e1 >= e2: res += 1
    return res

def part2():
    data = open('task4.txt', 'r').read().split('\n')
    res = 0
    for s in data:
        s = s.split(',')
        s[0], s[1] = list(map(int, s[0].split('-'))), list(map(int, s[1].split('-')))
        s.sort(key=lambda x: (x[0], -x[1]))
        s1, e1, s2, e2 = s[0][0], s[0][-1], s[1][0], s[1][-1]

        if e1 >= s2: res += 1
    return res


if __name__ == '__main__':
    print(task4())
    print(part2())