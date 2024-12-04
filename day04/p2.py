from typing import List
from collections import defaultdict

def create(board, r, c, diffs):
    ROWS = len(board)
    COLS = len(board[0])
    s = []
    while 0 <= r < ROWS and 0 <= c < COLS:
        s.append((r, c))
        r += diffs[0]
        c += diffs[1]
    return s

def find(board, s):
    coords = []
    ln = [board[r][c] for r, c in s]
    strs = [''.join(ln[i:]) for i in range(len(ln))]
    for i, ln in enumerate(strs):
        if ln.startswith("MAS"): coords.append(s[i + 1])
        elif ln.startswith("SAM"): coords.append(s[i + 1])
    return coords

def create_all(board):
    ROWS = len(board)
    COLS = len(board[0])
    
    strs = []

    # diag \
    for i in range(ROWS):
        strs.append(create(board, i, 0, [1, 1]))
    for i in range(1, COLS):
        strs.append(create(board, 0, i, [1, 1]))
    # diag /
    for i in range(COLS):
        strs.append(create(board, 0, i, [1, -1]))
    for i in range(1, ROWS):
        strs.append(create(board, i, COLS - 1, [1, -1]))

    return strs
    
def solve(inp: List[str]):
    coords = defaultdict(lambda: 0)
    strs = create_all(inp)
    ans = 0

    for s in strs:
        cos = find(inp, s)
        for r, c in cos:
            coords[(r, c)] += 1
            if coords[(r, c)] == 2:
                ans += 1
    return ans