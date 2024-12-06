from typing import List

def solve(inp: List[str]):
    positions = set()
    points = set()
    cur = (0, 0)
    d = (-1, 0)
    for i, ln in enumerate(inp):
        for j, ch in enumerate(ln):
            if ch == '#': points.add((i, j))
            elif ch != '.':
                cur = (i, j)
                if ch == '^': d = (-1, 0)
                elif ch == '>': d = (0, 1)
                elif ch == 'v': d = (1, 0)
                elif ch == '<': d = (0, -0)
    (i, j) = cur
    ROWS = len(inp)
    COLS = len(inp[0])
    def inside(): return 0 <= i < ROWS and 0 <= j < COLS
    while inside(): # and not (i, j, d) in positions_rot:
        positions.add((i, j))
        new_i = i + d[0]
        new_j = j + d[1]
        if not inside(): break
        if (new_i, new_j) in points:
            d = (d[1], -d[0])
        else:
            i = new_i
            j = new_j
    return len(positions)
