from typing import List

def run_slow(board, cur, points, d):
    positions = set()
    positions_rot = set()
    (i, j) = cur
    ROWS = len(board)
    COLS = len(board[0])
    def inside(): return 0 <= i < ROWS and 0 <= j < COLS
    while inside() and (i, j, d) not in positions_rot:
        positions.add((i, j))
        positions_rot.add((i, j, d))
        new_i = i + d[0]
        new_j = j + d[1]
        if not inside(): break
        if (new_i, new_j) in points:
            d = (d[1], -d[0])
        else:
            i = new_i
            j = new_j
        # print(i, j)
    return (positions, (i, j, d) in positions_rot)

def solve_slow(inp: List[str]):
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
    
    path_points, _ = run_slow(inp, cur, points, d)

    ans = 0
    for r, c in path_points:
        points.add((r, c))
        _, loop = run_slow(inp, cur, points, d)
        points.remove((r, c))

        if loop: ans += 1
    return ans

# New faster solution 
ans = 0
def run(board, cur, points, d, positions_rot, changed):
    global ans

    tried = set()
    (i, j) = cur
    ROWS = len(board)
    COLS = len(board[0])
    while 0 <= i < ROWS and 0 <= j < COLS and (i, j, d) not in positions_rot:
        new_i = i + d[0]
        new_j = j + d[1]

        if (new_i, new_j) in points:
            positions_rot.add((i, j, d))
            d = (d[1], -d[0])
        else:
            if not changed and not (new_i, new_j) in tried:
                points.add((new_i, new_j))
                # note: we could use two separate sets, but it turns out copying is faster
                # informally, if n are the number of currently discovered points and k are
                # the points to be discovered, copying takes O(n) read/writes and O(k(n+k)) writes/accesses
                # but maintaining two sets takes O(k*k) + O(k*n) = O(k^2 + nk) accesses and O(k^2) writes.
                # It seems the extra overhead in the latter is slower
                run(board, (i, j), points, d, positions_rot.copy(), True)
                points.remove((new_i, new_j))
                tried.add((new_i, new_j))
            positions_rot.add((i, j, d))
            i = new_i
            j = new_j
    if (i, j, d) in positions_rot:
        ans += 1

def solve(inp: List[str]):
    global ans

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
    
    ans = 0
    run(inp, cur, points, d, set(), False)
    return ans
        
