from typing import List

# ORIGINAL SLOW SOLUTION
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

# SMARTER SOLUTION
def has_safe_smart(ln):
    s = [int(x) for x in ln.split()]
    diff = []
    for i in range(len(s) - 1):
        diff.append(s[i + 1] - s[i])
    
    neg = sum([1 for x in diff if x < 0])
    if neg >= len(diff) - 2:
        diff = [-x for x in diff]
    
    fixed = 0
    for i, d in enumerate(diff):
        if 1 <= d <= 3: continue
        if fixed >= 1: return False
        
        fixed += 1
        # IMPORTANT: always try to combine with the later step (i.e. delete the later level) first!
        # if the previous steps were already fine, only combine them if needed 
        if i < len(diff) - 1 and 1 <= d + diff[i + 1] <= 3: # delete level in front
            diff[i + 1] += d
        elif i > 0 and 1 <= diff[i - 1] + d <= 3: # delete level behind
            pass
        elif i == len(diff) - 1 or i == 0: # if at either endpoint, nothing we can do but delete the current level
            pass
        else:
            return False
    return True


def solve(inp: List[str]):
    ans = 0
    for ln in inp:
        ans += has_safe_smart(ln)
    return ans