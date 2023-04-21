# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import heapq



def splitChar(arr):
    res = []
    j = 0
    for i in range(len(arr)):
        if arr[i] == '':
            res.append(arr[j:i])
            j = i+1
    return res

def task1():
    data = open('task1.txt', 'r').read().split('\n')
    data = splitChar(data)
    topthree = []
    for i in range(len(data)):
        sum = 0
        for c in data[i]:
            sum+=(int)(c)

        heapq.heappush(topthree,sum)
        if len(topthree) > 3:
            heapq.heappop(topthree)
    res = 0
    for i in topthree:
        res+=i
    return res



if __name__ == '__main__':
    print(task1())
