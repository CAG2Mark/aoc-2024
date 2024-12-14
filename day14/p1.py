from typing import List
import re
def solve(inp: List[str]):
    ROWS = 103
    COLS = 101
    robots = []
    for ln in inp:
        s = ln.split()
        s1 = s[0][2:]
        s2 = s[1][2:]
        c, r = (int(x) for x in s1.split(","))
        dc, dr = (int(x) for x in s2.split(","))
        robots.append((r, c, dr, dc))
    SECS = 100
    new_robots = []
    for _ in range(SECS):
        for r, c, dr, dc in robots:
            r = (r + dr) % ROWS
            c = (c + dc) % COLS
            new_robots.append((r, c, dr, dc))
        robots = new_robots
        new_robots = []
    q = [[0, 0], [0, 0]]
    for r, c, _, _, in robots:        
        h = 0
        v = 0
        if r == ROWS // 2: continue
        elif r > ROWS // 2: h = 1
        if c == COLS // 2: continue
        elif c > COLS // 2: v = 1
        q[h][v] += 1
    print(q)
    prod = 1
    for l in q:
        for v in l:
            prod *= v
    
    return prod