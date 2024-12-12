from typing import List
from collections import defaultdict

def solve(inp: List[str]):
    points = defaultdict(lambda: [])
    all_points = set()
    antidotes = set()
    for i, ln in enumerate(inp):
        for j, ch in enumerate(ln):
            if ch == '.': continue
            points[ch].append((i, j))
            all_points.add((i, j))
    ROWS = len(inp)
    COLS = len(inp[0])
    
    def valid(p): 
        return 0 <= p[0] < ROWS and 0 <= p[1] < COLS

    for ch, ls in points.items():
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                i1, j1 = ls[i]
                i2, j2 = ls[j]
                d1 = i2 - i1
                d2 = j2 - j1
                pi = (i2 + d1, j2 + d2)
                pj = (i1 - d1, j1 - d2)
                if valid(pi): antidotes.add(pi)
                if valid(pj): antidotes.add(pj)
    
    return len(antidotes)