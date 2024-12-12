from typing import List
from collections import defaultdict

def neighbours(board, i, j):
    ROWS = len(board)
    COLS = len(board[0])

    dels = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in dels:
        ni = i + dr
        nj = j + dc
        if not (0 <= ni < ROWS and 0 <= nj < COLS): continue
        val = board[i][j]
        nval = board[ni][nj]
        if nval - val != 1: continue
        yield((ni, nj))

def reachable(board, i, j):
    cnt = 0
    st = [(i, j)]
    visited = set()
    while st:
        cur = st.pop()
        visited.add(cur)
        if board[cur[0]][cur[1]] == 9: 
            cnt += 1
            continue
        for ni, nj in neighbours(board, *cur):
            if (ni, nj) in visited: continue
            st.append((ni, nj))
    return cnt

def solve(inp: List[str]):
    board = [[-10 if x == '.' else int(x) for x in ln] for ln in inp]
    total = 0
    for i, ln in enumerate(board):
        for j, val in enumerate(ln):
            if val == 0:
                total += reachable(board, i, j)
    return total