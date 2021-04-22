import pdb #Debug

def add(res, tupla):
    if len(res) > 0:
        if res[-1][1] == tupla[1]:
            return
        if res[-1][0] == tupla[0]:
            res[-1] = (res[-1][0], max(res[-1][1], tupla[1]))
            return
    res.append(tupla)

def mergePL(a, b):
    res = []
    i, j = 0, 0
    Na, Nb = len(a), len(b)
    yleft, yright = 0, 0
    while i < Na or j < Nb:
        if j >= Nb or i < Na and a[i][0] < b[j][0]:
            x, yleft = a[i]
            i += 1
        else:
            x, yright = b[j]
            j += 1
        ymax = max(yleft, yright)
        add(res, (x, ymax))
    return res

def skyline(rects: list, i, f):
    if i == f:
        g, h, d = rects[i]
        return [(g, h), (d,0)]
    mid = (i + f) // 2
    pl1 = skyline(rects, i, mid)
    pl2 = skyline(rects, mid + 1, f)
    return mergePL(pl1, pl2)

rects = [(3, 13, 9), (1, 11, 5), (19, 18, 22), (3, 6, 7), (16, 3, 25), (12, 7, 16)]

print(skyline(rects, 0, len(rects) - 1))