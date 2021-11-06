N = int(input())
cards = list(map(int,input().split()))
numM = int(input())
find_cards = list(map(int,input().split()))

cards.sort()


cnt = {}
results = []
for i in cards:
    try: cnt[i] += 1
    except: cnt[i] =1

for i in find_cards:
    if i in cnt.keys():
        #print(i,cnt[i])
        results.append(str(cnt[i]))
    else:
        #print(i,0)
        results.append("0")

print (" ".join(results))