def task5():
    data = open('task5.txt', 'r').read().split('\n')
    idx = -1
    for i,row in enumerate(data):
        if not row: idx = i
    stacks = []
    size = int(data[idx-1].split(' ')[-1])
    for i in range(1,size*4,4):
        stack = []
        for j in range(idx-2,-1,-1):
            if i + 1 < len(data[j]):
                if data[j][i] != ' ':
                    stack.append(data[j][i])
        stacks.append(stack)

    for i in range(idx+1,len(data)):
        tmp = list(map(lambda x : int(x) if x.isnumeric() else x, data[i].split(' ')))
        quantity, source, dest = tmp[1], tmp[3], tmp[5]
        for j in range(quantity):
            stacks[dest-1].append(stacks[source-1].pop())
    res = []
    for stack in stacks:
        res.append(stack[-1])
    return res


def visualize_stacks(stacks):
    st = []
    print(len(stacks))
    for col in range(len(stacks)):
        tmp = []
        for row in range(len(stacks)):
            if len(stacks[row]) > col:
                tmp.append(stacks[row][col])
            else:
                tmp.append(' ')
        st.append(list(map(lambda x: f'[{x}]' if x != ' ' else '   ', tmp)))
    st.reverse()
    for s in st:
        print(' '.join(s))
    for i in range(len(st)):
        print(f' {i+1}  ', end ='')
    print('')

def part2():
    data = open('task5.txt', 'r').read().split('\n')
    idx = -1
    for i, row in enumerate(data):
        if not row: idx = i
    stacks = []
    size = int(data[idx - 1].split(' ')[-1])
    for i in range(1, size * 4, 4):
        stack = []
        for j in range(idx - 2, -1, -1):
            if i + 1 < len(data[j]):
                if data[j][i] != ' ':
                    stack.append(data[j][i])
        stacks.append(stack)
    for i in range(idx + 1, len(data)):
        tmp = list(map(lambda x: int(x) if x.isnumeric() else x, data[i].split(' ')))
        quantity, source, dest = tmp[1], tmp[3], tmp[5]
        order_stack = []
        for j in range(quantity):
            order_stack.append(stacks[source - 1].pop())
        for _ in range(len(order_stack)):
            stacks[dest - 1].append(order_stack.pop())
        visualize_stacks(stacks)
    res = []
    for stack in stacks:
        res.append(stack[-1])
    return res


if __name__ == '__main__':
    print(task5())
    print(part2())