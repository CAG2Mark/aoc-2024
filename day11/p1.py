from typing import List

def solve(inp: List[str]):
    inp = inp[0]
    stones = [int(x) for x in inp.split()]
    new_stones = []
    for i in range(25):
        for s in stones:
            if s == 0:
                new_stones.append(1)
            elif len(str(s)) % 2 == 1:
                new_stones.append(s * 2024)
            else:
                st = str(s)
                s1 = int(st[:len(st) // 2])
                s2 = int(st[len(st) // 2:])
                new_stones.append(s1)
                new_stones.append(s2)
        stones = new_stones
        new_stones = []
    return len(stones)
