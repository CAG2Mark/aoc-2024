from typing import List

def solve(inp: List[str]):
    board = inp
    ans = 0
    ROWS = len(board)
    COLS = len(board[0])
    s = set()
    for i in range(ROWS):
        for j in range(COLS):
            s.add((i, j))
    parts = []
    while s:
        perim = 0
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
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni = i + di
                nj = j + dj
                if not (0 <= ni < ROWS and 0 <= nj < COLS):
                    perim += 1
                    continue
                if ch != board[ni][nj]:
                    perim += 1
                    continue
                if (ni, nj) in v: continue
                st.add((ni, nj))
        ans += perim * len(v)
    return ans