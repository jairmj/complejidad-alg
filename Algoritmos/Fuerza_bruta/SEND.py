def replace(a, equivalence):
    s = 0
    for c in a:
        s = s * 10 + equivalence[c]
    return s

def validate(a, b, c, equivalence):
    na = replace(a, equivalence)
    nb = replace(b, equivalence)
    nc = replace(c, equivalence)
    return na + nb == nc
        

equivalence = {
    's' : 0,
    'n' : 1,
    'd' : 2,
    'y' : 3,
    'e' : 4,
    'm' : 5,
    'r' : 6,
    'o' : 7
}

def makeEquivalence(dic, s, n, d, y, e, m, r, o):
    dic['s'] = s
    dic['n'] = n
    dic['d'] = d
    dic['y'] = y
    dic['e'] = e
    dic['m'] = m
    dic['r'] = r
    dic['o'] = o



equivalence1 = {}
solutions = 0

for s in range(10):
    for n in range(10):
        for d in range(10):
            for y in range(10):
                for e in range(10):
                    for m in range(10):
                        for r in range(10):
                            for o in range(10):
                                makeEquivalence(equivalence1, s, n, d, y, e, m, r, o)
                                if validate("send", "more", "money", equivalence1):
                                    print("{} + {} = {}".format([s,e,n,d], [m,o,r,e], [m,o,n,e,y]))
                                    solutions+=1



print("Soluciones: {}".format(solutions))