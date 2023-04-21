import sys


class Dir:
    def __init__(self, name):
        self.files = {}
        self.dirs = set()
        self.name = name

    def get_value(self):
        res = 0
        for file in self.files:
            res += int(self.files[file])

        for dir in self.dirs:

            res += dir.get_value()
        return res

    def add_file(self,file):
        self.files[file[0]] = file[1]

    def add_dir(self,dir):
        self.dirs.add(dir)

    def __str__(self):
        return self.name

    def visualize(self):
        dir_names = list(map(lambda x: x.name, self.dirs))
        file_names = list(map(lambda x: x[0] , self.files.items()))
        print(self.name,': ' , ', '.join(dir_names), ' | ',', '.join(file_names))


def task7():
    data = open('task7.txt', 'r').read().split('\n')
    data = list(map(lambda x : x.split(' '),data))
    path = ['root']
    glb_dirs = {}
    for i in range(len(data)):
        d = data[i]
        if d[0] == '$':
            if d[1] == 'cd':
                if d[2] == '..':
                    path.pop()
                else:
                    if (d[2],path[-1]) not in glb_dirs:
                        glb_dirs[(d[2],path[-1])] = (Dir(d[2]))
                    if d[2] == '/':
                        path = ['root']
                    path.append(glb_dirs[(d[2],path[-1])])
        else:
            if d[0] == 'dir':
                if (d[1], path[-1]) not in glb_dirs:
                    glb_dirs[(d[1],path[-1])] = (Dir(d[1]))
                path[-1].add_dir(glb_dirs[(d[1],path[-1])])
            else:
                path[-1].add_file((d[1],d[0]))
    res = 0
    for name, dir in glb_dirs.items():
        v = dir.get_value()
        if v <= 100000:
            res += v


    return res



def part2():
    data = open('task7.txt', 'r').read().split('\n')
    data = list(map(lambda x: x.split(' '), data))
    path = ['root']
    glb_dirs = {}
    for i in range(len(data)):
        d = data[i]
        if d[0] == '$':
            if d[1] == 'cd':
                if d[2] == '..':
                    path.pop()
                else:
                    if (d[2], path[-1]) not in glb_dirs:
                        glb_dirs[(d[2], path[-1])] = (Dir(d[2]))
                    if d[2] == '/':
                        path = ['root']
                    path.append(glb_dirs[(d[2], path[-1])])
        else:
            if d[0] == 'dir':
                if (d[1], path[-1]) not in glb_dirs:
                    glb_dirs[(d[1], path[-1])] = (Dir(d[1]))
                path[-1].add_dir(glb_dirs[(d[1], path[-1])])
            else:
                path[-1].add_file((d[1], d[0]))
    res = sys.maxsize
    needed = 30000000 - (70000000 - glb_dirs[('/','root')].get_value())
    for name, dir in glb_dirs.items():
        v = dir.get_value()
        print(v,needed)
        if v >= needed:
            res = min(res, v)

    return res




if __name__ == '__main__':
    print(task7())
    print(part2())