from typing import List
from collections import defaultdict
from functools import cache

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

def solve(inp: List[str]):
    board = [[-10 if x == '.' else int(x) for x in ln] for ln in inp]
    total = 0

    @cache
    def count(i, j):
        if board[i][j] == 9: return 1
        ans = 0
        for ni, nj in neighbours(board, i, j):
            ans += count(ni, nj)
        return ans

    for i, ln in enumerate(board):
        for j, val in enumerate(ln):
            if val == 0:
                total += count(i, j)
    return total