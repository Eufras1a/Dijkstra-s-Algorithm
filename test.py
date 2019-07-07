import math, time
graph = [
    [(2, 5), (3, 10), (4, 5)],
    [(1, 5), (3, 4)],
    [(1, 10), (2, 4), (4, 15)],
    [(1, 5), (3, 15)]
    
]

X = [False] * 4
A = [100000] * 4
X[0] = True
A[0] = 0

while True:
    old = math.inf

    for i in range(len(X)):
        if X[i]:
            for edge in graph[i]:
                if X[edge[0] - 1] == False:
                    new = A[i] + edge[1]

                    if old > new:
                        old = new
                        u = i
                        v = edge[0] - 1
    
    A[v] = old
    X[v] = True
    if not False in X:
        break

print(A)