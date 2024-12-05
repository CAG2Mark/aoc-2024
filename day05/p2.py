from typing import List
from collections import defaultdict

def solve(inp: List[str]):
    gt = set()

    queues = []
    i = 0
    while i < len(inp):
        ln = inp[i]
        if not ln:
            i += 1
            break
        s = ln.split("|")
        gt.add((int(s[1]), int(s[0])))
        i += 1
        
    while i < len(inp):
        ln = inp[i]
        queues.append([int(x) for x in ln.split(",")])
        i += 1

    ans = 0

    def good(q):
        L = len(q)
        for i in range(L):
            for j in range(i + 1, L):
                if (q[i], q[j]) in gt: return False
        return True

    for q in queues:
        if good(q): continue
        L = len(q)
        # sort
        for i in range(L):
            for j in range(i + 1, L):
                if (q[i], q[j]) in gt:
                    tmp = q[j]
                    q[j] = q[i]
                    q[i] = tmp

        ans += q[len(q) // 2]
                
    
    return ans