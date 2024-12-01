from typing import List

def solve(inp: List[str]):
    l1 = []
    l2 = []
    for ln in inp:
        s = ln.split()
        l1.append(int(s[0]))
        l2.append(int(s[1]))
    s = 0
    l1.sort()
    l2.sort()
    for (a, b) in zip(l1, l2):
        s += abs(a - b)
    return s