from typing import List

def safe(s):
    diff = []
    for i in range(len(s) - 1):
        diff.append(s[i + 1] - s[i])
    if diff[0] < 0: 
        diff = [-x for x in diff]
        
    return all([1 <= d <= 3 for d in diff])

def has_safe(ln):
    s = [int(x) for x in ln.split()]
    # lazy solution, just guess and check which one to delete :P
    for i in range(len(s)):
        c = s.copy()
        del c[i]
        if safe(c):
            return True
    return False

def solve(inp: List[str]):
    ans = 0
    for ln in inp:
        ans += has_safe(ln)
    return ans