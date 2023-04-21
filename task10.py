def task10():
    data = open('task10.txt', 'r').read().split('\n')
    cycle_count = 0
    res = 0
    x = 1

    def cycle():
        nonlocal  cycle_count
        nonlocal res
        cycle_count += 1
        if not (cycle_count-20) % 40:
            res += cycle_count * x


    for line in data:
        line = line.split(' ')
        if line[0] == 'noop':
            cycle()
        elif line[0] == 'addx':
            cycle()
            cycle()
            x += int(line[1])
    return res

def part2():
    data = open('task10.txt', 'r').read().split('\n')
    cycle_count = 0
    x = 1
    row = 0
    crt = [['.' for _ in range(40)] for _ in range(6)]

    def cycle():
        nonlocal  cycle_count
        nonlocal row
        if x-1 <= cycle_count <= x+1:
            crt[row][cycle_count] = '#'
        cycle_count += 1

        if not cycle_count % 40:
            print(cycle_count)
            cycle_count = 0
            row+=1

    for line in data:
        line = line.split(' ')
        if line[0] == 'noop':
            cycle()
        elif line[0] == 'addx':
            cycle()
            cycle()
            x += int(line[1])
    return crt

if __name__ == '__main__':
    print(task10())
    for line in part2():
        print(line)
