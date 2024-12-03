from typing import List
import re

r = re.compile(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)")

def solve_line(ln):
    ans = 0
    do = True
    for a, b, c, d in r.findall(ln):
        if c: do = True
        elif d: do = False
        elif do:
            ans += int(a) * int(b)
    return ans

def solve(inp: List[str]):
    ans = 0
    return solve_line(''.join(inp))