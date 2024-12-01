from typing import List

def solve(inp: List[str]):
    l1 = []
    l2 = []
    for ln in inp:
        s = ln.split()
        l1.append(int(s[0]))
        l2.append(int(s[1]))
    s = 0
    cntr = {}
    for i in l1:
        cntr[i] = 0
    for i in l2:
        if not i in cntr: continue
        cntr[i] += 1

    for (a, b) in cntr.items():
        s += a * b
    return s