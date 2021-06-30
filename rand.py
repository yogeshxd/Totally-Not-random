import struct
import time

def lastbit(f):
    return struct.pack('!f', f)[-1] & 1

def getrandbits(k):
    "Return k random bits using a relative drift of two clocks."
    result = 0
    for _ in range(k):
        time.sleep(0)
        result <<= 1
        result |= lastbit(time.perf_counter())
    return result

def randbelow(n):
    "Return a random int in the range [0,n).  Raises ValueError if n<=0."
    # from Lib/random.py
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    r = getrandbits(k)
    while r >= n:
        r = getrandbits(k)
    return r


def randint(a, b):
    "Return random integer in range [a, b], including both end points."
    return a + randbelow(b - a + 1)

print(*[randint(10, 110) for _ in range(5)])