from typing import List


def get(a1, b1, a2, b2, x, y):
    # consider the intersection of the lines (a1, b1)t, (x, y) - (a2, b2)t
    # a1 a2
    # b1 b2

    det = a1 * b2 - a2 * b1
    if det == 0: return 0
    inverse = [
        [ b2, -a2],
        [-b1,  a1]
    ]
    t = inverse[0][0] * x + inverse[0][1] * y
    s = inverse[1][0] * x + inverse[1][1] * y
    if t % det != 0 or s % det != 0: return 0

    return 3 * t // det + s // det


def solve(inp: List[str]):
    i = 0
    sm = 0
    while i < len(inp):
        def parsebtn():
            ln = inp[i]
            _, _, c, d = ln.split()
            a, b = int(c[2:-1]), int(d[2:])
            return a, b
        def parseprize():
            ln = inp[i]
            _, b, c = ln.split()
            x, y = int(b[2:-1]), int(c[2:])
            x += 10000000000000
            y += 10000000000000
            return x, y
        a1, b1 = parsebtn()
        i += 1
        a2, b2 = parsebtn()
        i += 1
        x, y = parseprize()
        i += 2
        sm += get(a1, b1, a2, b2, x, y)
    return sm