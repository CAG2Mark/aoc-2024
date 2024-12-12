from typing import List
from collections import defaultdict

def solve(inp: List[str]):
    inp = inp[0]
    stones = [int(x) for x in inp.split()]
    stones_dict = defaultdict(lambda: 0)
    for s in stones:
        stones_dict[s] += 1
    new_stones = defaultdict(lambda: 0)
    for i in range(75):
        for s, cnt in stones_dict.items():
            if s == 0:
                new_stones[1] += cnt
            elif len(str(s)) % 2 == 1:
                new_stones[s * 2024] += cnt
            else:
                st = str(s)
                s1 = int(st[:len(st) // 2])
                s2 = int(st[len(st) // 2:])
                new_stones[s1] += cnt
                new_stones[s2] += cnt
        stones_dict = new_stones
        new_stones = defaultdict(lambda: 0)
    sm = 0
    for cnt in stones_dict.values(): sm += cnt
    return sm
