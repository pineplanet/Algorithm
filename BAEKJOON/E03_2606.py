import sys
from collections import deque

N = int(input())
Links = int(input())

nodes = {}
for i in range(Links):
    k,v = map(int, sys.stdin.readline().split())
    try: nodes[k].append(v)
    except: nodes[k] = [v]

    if v not in nodes:
        nodes[v]= [k]
    else:
        if k not in nodes[v]:
            nodes[v].append(k)

bfs = deque([1])
b_visited = []
while bfs:
    node = bfs.popleft()
    if node not in b_visited:
        b_visited.append(node)
        try:
            bfs.extend(nodes[node])
        except:
            pass

print(len(b_visited)-1)