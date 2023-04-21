def is_touching(head, tail):
    dirs = [[0,0],[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,1],[1,-1],[-1,1]]
    hx,hy = head
    tx,ty = tail
    for x,y in dirs:
        if tx+x == hx and ty+y == hy: return True
    return False

def fix_tail(head, tail):
    hx, hy = head
    tx, ty = tail
    res = [tx,ty]
    if tx == hx:
        res[1] += 1 if hy-ty > 0 else -1
    elif ty == hy:
        res[0] += 1 if hx - tx > 0 else -1
    else:
        res[0] += 1 if hx - tx > 0 else -1
        res[1] += 1 if hy - ty > 0 else -1
    return res



def task9():
    data = open('test.txt','r').read().split('\n')
    print(data)
    visited = set([(0,0)])
    head, tail = [0,0], [0,0]
    horizontal, vertical = 0, 0
    for s in data:
        t = s.split(' ')
        direction, amount = t[0], int(t[1])
        idx, dir = 0,0
        if direction == 'R':
            idx, dir = 1,1
        elif direction == 'L':
            idx, dir = 1,-1
        elif direction == 'U':
            idx, dir = 0,-1
        elif direction == 'D':
            idx, dir = 0,1
        for _ in range(amount):
            head[idx] += dir
            if not is_touching(head, tail):
                tail = fix_tail(head, tail)
            visited.add(tuple(tail))
            print(head, tail)
    return len(visited)


def part2():
    data = open('task9.txt', 'r').read().split('\n')
    print(data)
    visited = set([(0, 0)])
    points = [[0,0] for _ in range(10)]
    for s in data:
        t = s.split(' ')
        direction, amount = t[0], int(t[1])
        idx, dir = 0,0
        if direction == 'R':
            idx, dir = 1,1
        elif direction == 'L':
            idx, dir = 1,-1
        elif direction == 'U':
            idx, dir = 0,-1
        elif direction == 'D':
            idx, dir = 0,1
        for _ in range(amount):
            points[0][idx] += dir
            for i in range(1, len(points)):
                if not is_touching(points[i-1], points[i]):
                    points[i] = fix_tail(points[i-1], points[i])
            visited.add(tuple(points[-1]))
    return len(visited)


if __name__ == '__main__':
    print(task9())
    print(part2())