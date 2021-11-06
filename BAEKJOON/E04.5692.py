import math
import sys

while 1:
    N = sys.stdin.readline().rstrip()

    if N == '0':
        break
    s = 0
    for i in range(len(N)):
        j = int(N[i])
        s += (j * math.factorial(len(N) - i))

    print(s)
