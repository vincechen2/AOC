def task3():
    data = open('task3.txt', 'r').read().split('\n')
    lower_cmp = ord('a') - 1
    upper_cmp = ord('A') - 27
    res = 0
    for rucksack in data:
        mid = len(rucksack)// 2
        same = find_match(rucksack[:mid],rucksack[mid:])
        res += ord(same)-upper_cmp if same.isupper() else ord(same)-lower_cmp
    return res

def find_match(s1,s2):
    seen = set([c for c in s1])
    for c in s2:
        if c in seen: return c

def find_match3(s1,s2,s3):
    seen = set([c for c in s1])
    seen2 = set([c for c in s2 if c in seen])
    for c in s3:
        if c in seen2: return c

def part2():
    data = open('task3.txt', 'r').read().split('\n')
    lower_cmp = ord('a') - 1
    upper_cmp = ord('A') - 27
    res = 0
    for i in range(0,len(data),3):
        same = find_match3(data[i],data[i+1],data[i+2])
        res += ord(same) - upper_cmp if same.isupper() else ord(same) - lower_cmp
    return res


if __name__ == '__main__':
    print(task3())
    print(part2())