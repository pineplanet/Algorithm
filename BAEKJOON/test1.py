#평행 이동 move1 = (x + y) * w #짝수, 홀수에 따른 이동 if (x + y) % 2 == 0: #x + y가 짝수라면 move2 = max(x, y) * s else: #홀수라면 move2 = (max(x, y) - 1) * s + w #대각선 + 평행 이동 move3 = (min(x, y) * s) + ((max(x, y) - min(x, y)) * w) res = min(min(move1, move2), move3) print(res)

x = 4
y = 2
w = 3
s = 10

move1 = (x+1)*w

if (x+y) %2 ==0:
    move2 = max(x,y)*s

else:
    move2 = (max(x, y) - 1) * s + w

move3 = (min(x, y) * s) + ((max(x, y) - min(x, y)) * w)

res = min(min(move1, move2), move3)
print(res)