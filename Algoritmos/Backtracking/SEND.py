
def replace(a, equivalence):
    s = 0
    for c in a:
        s = s * 10 + equivalence[c]
    return s

def validate(a, b, c, codex, chars):
    for i in range(len(codex)):
        a = a.replace(chars[i], str(codex[i]))
        b = b.replace(chars[i], str(codex[i]))
        c = c.replace(chars[i], str(codex[i]))
    if int(a) + int(b) == int(c):
        print(a,b,c)

def combinations(digits, n, w, chars, codex, a, b, c):
    if w == n:
        validate(a, b, c, codex, chars)
    else:
        for i in range(len(digits)):
            e = digits[i]
            print(digits[:i], digits[i+1:])
            print(e, i)
            combinations(digits[:i] + digits[i+1:], n, w + 1, chars, codex+[e], a, b, c)

def solve(a, b, c):
    chars = list(set(a + b + c))
    digits = [i for i in range(10)]
    n = len(chars)
    combinations(digits, n, 0, chars, [], a, b, c)

solve("SEND", "MORE", "MONEY")