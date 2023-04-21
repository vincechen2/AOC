from functools import reduce

def task8():
    data = open('task8.txt', 'r').read().split('\n')
    data = [[int(c) for c in s] for s in data]
    res = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if is_visible(row,col,data):
                res += 1
    return res



def is_visible(i,j,arr):
    dirs = [-1,-1,-1,-1]
    for r in range(len(arr)):
        if r > i:
            dirs[1] = max(dirs[1],arr[r][j])
        elif r < i:
            dirs[0] = max(dirs[0],arr[r][j])
    for c in range(len(arr[0])):
        if c > j:
            dirs[3] = max(dirs[3], arr[i][c])
        elif c < j:
            dirs[2] = max(dirs[2], arr[i][c])

    return reduce(lambda acc, x : acc or x < arr[i][j], dirs, False)

def scenic_score(i,j,arr):
    dirs = [0  for _ in range(4)]
    for up in range(i-1,-1,-1):
        dirs[0] += 1
        if arr[up][j] >= arr[i][j]: break
    for down in range(i+1,len(arr)):
        dirs[1] += 1
        if arr[down][j] >= arr[i][j]: break
    for left in range(j-1,-1,-1):
        dirs[2] += 1
        if arr[i][left] >= arr[i][j]: break
    for right in range(j+1, len(arr)):
        dirs[3] += 1
        if arr[i][right] >= arr[i][j]: break
    print(f'({i},{j})',dirs)

    return reduce(lambda acc, x: acc*x,dirs,1)

def part2():
    data = open('task8.txt', 'r').read().split('\n')
    data = [[int(c) for c in s] for s in data]
    res = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            res = max(res,scenic_score(row,col,data))
    return res


if __name__ == '__main__':
    print(task8())
    print(part2())
