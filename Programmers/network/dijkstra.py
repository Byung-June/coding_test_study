
def dijkstra(K, V, graph):
    inf = 10000
    s = [False] * V
    d = [inf] * V
    d[K-1] = 0

    while True:
        m = inf
        N = -1

        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j

        if m == inf:
            break

        s[N] = True
        for j in range(V):
            if s[j]: continue
            via = d[N] + graph[N][j]
            if d[j] > via:
                d[j] = via

    return d


if __name__== '__main__':
    V, E = 5, 6
    K = 1
    inf = 10000
    g = [[inf] * V for _ in range(V)]
    W = [[5,1,1], [1,2,2], [1,3,3], [2,3,4], [2,4,5], [3,4,6]]
    for u, v, w in W:
         g[u-1][v-1] = w

    print(g)
    for k in range(1, V+1):
        print(dijkstra(k, V, g))

