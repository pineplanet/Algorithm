import sys

N = int(input())
B = sys.stdin.readline()

sum = 0
M= 1234567891
for i in range(N) :

    a = (ord(B[i])-96)
    b = 31**i
    sum += a*b

print( sum%M)