import sys


def floyd_warshall(V, graph):
    inf = sys.maxsize
    d = [[inf] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            d[i][j] = graph[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d
