from typing import List

def solve(inp: List[str]):
    walls = set()
    boxes = set()
    r, c = 0, 0
    ROWS = 0
    COLS = len(inp[0]) * 2
    for i, ln in enumerate(inp):
        if not ln: 
            ROWS = i
            break
        for j, ch in enumerate(ln):
            if ch == '#':
                walls.add((i, j * 2))
                walls.add((i, j * 2 + 1))
            elif ch == 'O': boxes.add((i, j * 2))
            elif ch == '@': r, c = i, j * 2
    moves = []
    for ln in inp[ROWS + 1:]:
        moves += list(ln)
    MAP = {
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
        '^': (-1, 0)
    }
    def print_map():
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) == (r, c): print('@', end='')
                elif (i, j) in walls:
                    print('#', end='')
                elif (i, j) in boxes:
                    print('[', end='')
                elif (i, j - 1) in boxes:
                    print(']', end='')
                else: 
                    print('.', end='')
            print()
        print()
    for m in moves:
        # print_map()
        dr, dc = MAP[m]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < ROWS and 0 <= nc < COLS): continue
        if (nr, nc) in walls: continue
        st = set()
        mv = set()
        if dc == 0:
            if (nr, nc) in boxes: st.add((nr, nc))
            elif (nr, nc - 1) in boxes: st.add((nr, nc - 1))
        elif dc == 1:
            if (nr, nc) in boxes: st.add((nr, nc))
        else:
            if (nr, nc - 1) in boxes: st.add((nr, nc - 1))
        blocked = False
        while st:
            nnr, nnc = st.pop()
            mv.add((nnr, nnc))
            around = set()
            check = set()
            if dc == 0:
                for i in range(-1, 2):
                    check.add((nnr + dr, nnc + i))
                for i in range(0, 2):
                    around.add((nnr + dr, nnc + i))
            elif dc == 1:
                check.add((nnr, nnc + 2))
                around.add((nnr, nnc + 2))
            else:
                check.add((nnr, nnc - 2))
                around.add((nnr, nnc - 1))
            if len(around.intersection(walls)) > 0:
                blocked = True
                break
            for (nnr, nnc) in check:
                if (nnr, nnc) in boxes: st.add((nnr, nnc))
        if blocked: continue
        r, c = nr, nc
        for nnr, nnc in mv:
            boxes.remove((nnr, nnc))
        for nnr, nnc in mv:
            boxes.add((nnr + dr, nnc + dc))
    # print_map()
    ans = 0
    for r, c in boxes:
        ans += r * 100 + c
    return ans