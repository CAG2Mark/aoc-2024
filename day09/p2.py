from typing import List

def solve(inp: List[str]):
    data = [int(x) for x in inp[0]]
    drive = []
    ident = 0
    i = 0
    empty = False

    total_files = 0

    while i < len(data):
        if empty:
            drive.append((-1, data[i]))
        else:
            drive.append((ident, data[i]))
            total_files += data[i]
            ident += 1
        empty = not empty
        i += 1

    def find_suitable_free(length, upper):
        for i, (file_id, l) in enumerate(drive):
            if i >= upper: break
            if file_id != -1: continue
            if l < length: continue
            return i
        return -1
    
    def find_next(idx):
        while drive[idx][0] == -1:
            idx -= 1
            if len(drive) + idx <= 0: break 
        return idx


    if drive[-1][0] == -1:
        drive.pop()

    cur = -1
    while True:
        work_id, work_len = drive[cur]
        assert work_id != -1

        next_free = find_suitable_free(work_len, len(drive) + cur)

        if next_free == -1:
            if work_id == 0: break
            cur = find_next(cur - 1)
            continue

        assert drive[next_free][0] == -1
        space = drive[next_free][1]
        if space == work_len:
            drive[next_free] = (work_id, work_len)
            drive[cur] = (-1, work_len)
        elif space > work_len:
            drive.insert(next_free + 1, (-1, space - work_len))
            drive[next_free] = (work_id, work_len)
            drive[cur] = (-1, work_len)
        # print(drive)
        if work_id == 0: break
        cur = find_next(cur - 1)
    
    ans = 0
    idx = 0
    for file_id, length in drive:
        for i in range(length):
            if file_id != -1:
                ans += idx * file_id
            idx += 1
    return ans
