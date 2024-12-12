from typing import List
from collections import defaultdict

def solve(inp: List[str]):
    board = inp
    ans = 0
    ROWS = len(board)
    COLS = len(board[0])
    s = set()
    for i in range(ROWS):
        for j in range(COLS):
            s.add((i, j))
    rot = [(1,0),(0, 1),(-1,0),(0,-1), (1, 0)]
    while s:
        convex = 0
        touching = set()
        i, j = s.pop()
        ch = board[i][j]
        v = set()
        st = set()
        st.add((i, j))
        while st:
            i, j = st.pop()
            if (i, j) in s:
                s.remove((i, j))
            v.add((i, j))

            def good(ni, nj):
                return 0 <= ni < ROWS and 0 <= nj < COLS and ch == board[ni][nj]
            for k in range(4):
                di1, dj1 = rot[k]
                di2, dj2 = rot[k+1]
                ni1 = i + di1
                nj1 = j + dj1
                ni2 = i + di2
                nj2 = j + dj2
                if not good(ni1, nj1) and not good(ni2, nj2):
                    convex += 1
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni = i + di
                nj = j + dj
                if not good(ni, nj):
                    touching.add((ni, nj))
                    continue
                if (ni, nj) in v: continue
                st.add((ni, nj))
        concave = 0
        for ti, tj in touching:
            for k in range(4):
                di1, dj1 = rot[k]
                di2, dj2 = rot[k+1]
                di3, dj3 = di1 + di2, dj1 + dj2
                ni1 = ti + di1
                nj1 = tj + dj1
                ni2 = ti + di2
                nj2 = tj + dj2
                ni3 = ti + di3
                nj3 = tj + dj3
                if (ni1, nj1) in v and (ni2, nj2) in v and (ni3, nj3) in v:
                    concave += 1
        ans += (convex + concave) * len(v)
    return ans