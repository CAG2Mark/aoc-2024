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

    # heuristic: if it's a christmas tree, it should be mostly one block
    def is_block_size_small(limit):
        s = set()
        blocks = 0
        for r, c, _, _ in robots:
            s.add((r, c))
        while s:
            r, c = s.pop()
            size = 0
            q = set([(r, c)])
            while q:
                r, c = q.pop()
                size += 1
                if (r, c) in s:
                    s.remove((r, c))
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr < ROWS and 0 <= nc < COLS): continue
                    if not (nr, nc) in s: continue
                    q.add((nr, nc))
            blocks += 1
            if blocks > limit: return False
        return True
    
    new_robots = []
    i = 0
    LIM = 200
    while True:
        for r, c, dr, dc in robots:
            r = (r + dr) % ROWS
            c = (c + dc) % COLS
            new_robots.append((r, c, dr, dc))
        robots = new_robots
        new_robots = []
        i += 1
        if is_block_size_small(LIM): break
    
    def print_board():
        s = set()
        for r, c, _, _ in robots:
            s.add((r, c))
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in s: print("#", end="")
                else: print(".", end="")
            print()

    # :)
    print_board()
    return i