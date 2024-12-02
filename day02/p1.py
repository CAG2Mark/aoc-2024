from typing import List

def solve(inp: List[str]):
    ans = 0
    for ln in inp:
        s = [int(x) for x in ln.split()]
        diff = []
        for i in range(len(s) - 1):
            diff.append(s[i + 1] - s[i])
        if diff[0] < 0: 
            diff = [-x for x in diff]
            
        ans += all([1 <= d <= 3 for d in diff])
    return ans