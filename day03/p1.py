from typing import List
import re

r = re.compile(r"mul\((\d+),(\d+)\)")

def solve_line(ln):
    ans = 0
    for a, b in r.findall(ln):
        ans += int(a) * int(b)
    return ans

def solve(inp: List[str]):
    ans = 0
    for ln in inp:
        ans += solve_line(ln)
    return ans