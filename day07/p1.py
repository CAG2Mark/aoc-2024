from typing import List
from functools import cache

@cache
def possible(test, vals, idx):
    if idx == 0: return test == vals[idx]
    if test < 0: return False

    return (test % vals[idx] == 0 and possible(test // vals[idx], vals, idx - 1))# or possible(test - vals[idx], vals, idx - 1)  

def solve(inp: List[str]):
    ans = 0
    for ln in inp:
        a, b = ln.split(": ")
        test = int(a)
        vals = tuple([int(x) for x in b.split()])
        if possible(test, vals, len(vals) - 1): ans += test
    return ans