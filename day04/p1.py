from typing import List

def create(board, r, c, diffs):
    ROWS = len(board)
    COLS = len(board[0])
    s = ""
    while 0 <= r < ROWS and 0 <= c < COLS:
        s += board[r][c]
        r += diffs[0]
        c += diffs[1]
    return s

def count(s):
    cnt = 0
    for i in range(len(s)):
        if s[i:].startswith("XMAS"): cnt += 1
        if s[i:].startswith("SAMX"): cnt += 1
    return cnt

def create_all(board):
    ROWS = len(board)
    COLS = len(board[0])
    
    strs = []

    # horizontal
    for i in range(ROWS):
        strs.append(create(board, i, 0, [0, 1]))
    for i in range(COLS):
        strs.append(create(board, 0, i, [1, 0]))
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
    ans = 0
    strs = create_all(inp)

    for s in strs:
        ans += count(s)

    return ans