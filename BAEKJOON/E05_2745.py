import sys

N, B = sys.stdin.readline().rstrip().split()
NLength = len(N)
sum = 0

for i in range(NLength):
    if N[i].isupper():

        a = (ord(N[i]) - 55)
    else:
        a = (ord(N[i]) - 48)
    b = int(B) ** (NLength - i - 1)
    sum += b * a

if sum < 1000000000 :
    print(sum)

print(int(N, int(B)))
