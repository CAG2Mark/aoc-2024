from typing import List

# Taken from https://gist.github.com/smac89/568dce4c17e4499d59a86888a764a9a1
# Taken in part from: https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/

def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1

    gcd,x1,y1 = gcdExtended(b%a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd,x,y

def get(a1, b1, a2, b2, x, y):
    # find t, s such that at + bs = x
    def solve_axis(a, b, x):
        sols = set()
        
        # at + bs = d
        d, t, s = gcdExtended(a, b)

        # no solution
        if x % d != 0: return sols

        # initial solution: atX + bsX = x
        X = x // d
        t *= X
        s *= X 

        # get one of the solutions to become non-negative
        # note a * b / gcd(a, b) - b * a / gcd(a, b) = 0
        dt = b // d
        ds = a // d
        while t < 0:
            t += dt
            s -= ds
        
        print(dt, ds)
        
        # now let's reduce t to be as small as it can be
        while t >= 0:
            t -= dt
            s += ds

        # now generate all positive solutions!  
        # t is already as small as can be, so let's reduce the size of s
        while s >= 0:
            assert(a * t + b * s == x)
            sols.add((t, s))
            t += dt
            s -= ds
        
        return sols
    
    asols = solve_axis(a1, a2, x)
    bsols = solve_axis(b1, b2, y)

    print(asols)

    sols = asols.intersection(bsols)
    if not sols: return 0
    return min([3 * x + y for x, y in sols])


def solve(inp: List[str]):
    i = 0
    sm = 0
    while i < len(inp):
        def parsebtn():
            ln = inp[i]
            _, _, c, d = ln.split()
            a, b = int(c[2:-1]), int(d[2:])
            return a, b
        def parseprize():
            ln = inp[i]
            _, b, c = ln.split()
            x, y = int(b[2:-1]), int(c[2:])
            return x, y
        a1, b1 = parsebtn()
        i += 1
        a2, b2 = parsebtn()
        i += 1
        x, y = parseprize()
        i += 2
        sm += get(a1, b1, a2, b2, x, y)
    return sm