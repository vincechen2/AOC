from collections import deque

def task6():
    data = open('task6.txt', 'r').read()
    q = deque()
    cur = set()
    for i,c in enumerate(data):

        while c in cur:
            cur.remove(q.popleft())
        q.append(c)
        cur.add(c)
        if len(q) == 14:
            return i+1


if __name__ == '__main__':
    print(task6())
