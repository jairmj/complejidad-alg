import random
import numpy as np

class DisjointSet:
    def __init__(self, n):
        self.s = [-1]*n

    def find(self, a):
        if self.s[a] < 0:
            return a
        parent = self.find(self.s[a])
        self.s[a] = parent
        return parent

    def sameset(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        if self.sameset(a, b):
            return
        a = self.find(a)
        b = self.find(b)
        if -self.s[a] > -self.s[b]:
            self.s[a] += self.s[b]
            self.s[b] = a
        else:
            self.s[b] += self.s[a]
            self.s[a] = b

def makeMaze(rows, cols: int):
    maze = np.zeros((rows*2 + 1, cols*2+1))
    maze[1::2, 1::2] = 1
    maze[ 1][ 0] = 3
    maze[-2][-1] = 3

    walls = []
    walls.extend((i*cols+j, i*cols+j+1) for j in range(cols-1) for i in range(rows-1))
    walls.extend((i*cols+j, (i+1)*cols+j) for j in range(cols-1) for i in range(rows-1))
    walls.extend((i*cols+cols-1,(i+1)*cols+cols-1) for i in range(rows-1))
    walls.extend(((rows-1)*cols+j, (rows-1)*cols+j+1) for j in range(cols-1))

    s = DisjointSet(len(walls))
    random.shuffle(walls)
    while len(walls) > 0:
        e1, e2 = walls.pop()
        r1, c1 = e1 // cols, e1 % cols
        r2, c2 = e2 // cols, e2 % cols
        if not s.sameset(e1, e2):
            if r1 == r2 and c1 < c2:
                maze[r1*2+1][c1*2+2] = 1
            elif r1 == r2:
                maze[r1*2+1][c2*2+2] = 1
            elif c1 == c2 and r1 < r2:
                maze[r1*2+2][c1*2+1] = 1
            else:
                maze[r2*2+2][c1*2+1] = 1

            s.union(e1, e2)

    return maze