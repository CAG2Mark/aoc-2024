from typing import List

def solve(inp: List[str]):
    walls = set()
    boxes = set()
    r, c = 0, 0
    ROWS = 0
    COLS = len(inp[0])
    for i, ln in enumerate(inp):
        if not ln: 
            ROWS = i
            break
        for j, ch in enumerate(ln):
            if ch == '#': walls.add((i, j))
            elif ch == 'O': boxes.add((i, j))
            elif ch == '@': r, c = i, j
    moves = []
    for ln in inp[ROWS + 1:]:
        moves += list(ln)
    MAP = {
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
        '^': (-1, 0)
    }
    for m in moves:
        dr, dc = MAP[m]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < ROWS and 0 <= nc < COLS): continue
        if (nr, nc) in walls: continue
        nnr, nnc = nr, nc
        mv = set()
        while (nnr, nnc) in boxes:
            mv.add((nnr, nnc))
            nnr += dr
            nnc += dc
        if (nnr, nnc) in walls: continue
        r, c = nr, nc
        for nnr, nnc in mv:
            boxes.remove((nnr, nnc))
        for nnr, nnc in mv:
            boxes.add((nnr + dr, nnc + dc))
    ans = 0
    for r, c in boxes:
        ans += r * 100 + c
    return ans