# Abhijit Prakash Patil
# S20180010001

matrix = []
v = []

def bfs(s, t, n):
    flow = 1e8
    que = []
    que.append(s)
    global parent
    parent = [-1]*(n+1)
    parent[s] = -2
    global matrix
    global v

    while(len(que) > 0):
        temp = que[0]
        que.pop(0)
        for i in v[temp]:
            if parent[i] == -1 and matrix[temp][i] > 0:
                parent[i] = temp
                flow = min(flow, matrix[temp][i])
                if i == t:
                    return flow
                que.append(i)

    return 0

if __name__ == "__main__":
    maxFlow  = 0
    n = int(input())
    m = int(input())
    global matrix
    global v
    matrix = []
    for i in range(n+1):
        new = [0]*(n+1)
        matrix.append(new)
    v = [[]]*(n+1)

    for i in range(m):
        a = list(map(int, input().split()))
        v[a[0]].append(a[1])
        matrix[a[0]][a[1]] = a[2]

    s = 1
    t = n

    while(True):
        new_flow = bfs(s, t, n)
        global parent
        if new_flow <= 0:
            break
        temp = t
        par = parent[temp]
        while temp != s and temp != -1:
            matrix[par][temp] -= new_flow
            matrix[temp][par] += new_flow
            temp = par
            par = parent[par]
        maxFlow += new_flow

    print(maxFlow)

