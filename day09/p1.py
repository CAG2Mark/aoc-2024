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

    next_free = 1
    next_free_loc = drive[0][0]
    def get_next_free(idx):  
        tmp = next_free_loc
        while drive[idx][0] != -1:
            tmp += drive[idx][1]
            idx += 1
        return (idx, tmp)
    
    def find_next(idx):
        while drive[idx][0] == -1:
            idx -= 1
        return idx


    if drive[-1][0] == -1:
        drive.pop()

    cur = -1
    while next_free_loc < total_files:
        work_id, work_len = drive[cur]
        assert work_id != -1
        while work_len >= 0:
            assert drive[next_free][0] == -1
            space = drive[next_free][1]
            if space == work_len:
                drive[next_free] = (work_id, work_len)
                (next_free, next_free_loc) = get_next_free(next_free)
                break
            elif space > work_len:
                drive.insert(next_free + 1, (-1, space - work_len))
                drive[next_free] = (work_id, work_len)
                (next_free, next_free_loc) = get_next_free(next_free)
                break
            elif space < work_len:
                drive[next_free] = (work_id, space)
                work_len -= space
                (next_free, next_free_loc) = get_next_free(next_free)
        # print(drive)
        cur = find_next(cur - 1)
    
    ans = 0
    idx = 0
    for file_id, length in drive:
        for i in range(length):
            ans += idx * file_id
            idx += 1
            if idx == total_files: return ans
