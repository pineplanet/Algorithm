from collections import deque
import sys

input = sys.stdin.readline()

# 첫 줄
N,M,V = map(int,input.split())
nodes = {}
# 정점의 연결
for i in range(M):
    # 정점1과 연결된 자식1
    k, v = map(int, sys.stdin.readline().split())
    try: nodes[k].append(v)
    except : nodes[k] = [v]

    if v not in nodes:
        nodes[v] = [k]
    else:
        if k not in nodes[v]:
            nodes[v].append(k)

for key in nodes:
    nodes[key].sort()



#dfs
dfs = [V]
d_visited = []
while dfs:
    # 첫 노드 꺼냄
    node = dfs.pop()
    if node not in d_visited:
        d_visited.append(node)
        try:
            dfs.extend(sorted(nodes[node],reverse=True))
        except:
            pass

#bfs
bfs = deque([V])
b_visited = []
while bfs:
    node = bfs.popleft()
    if node not in b_visited:
        b_visited.append(node)
        try:
            bfs.extend(nodes[node])
        except:
            pass

##convert str
print(' '.join(map(str,d_visited)))
print(' '.join(map(str,b_visited)))
#print(b_visited)
