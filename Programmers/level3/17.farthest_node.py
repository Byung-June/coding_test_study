from collections import deque


def graph(vertex, n):
    g = {node: set([]) for node in range(1, n+1)}
    for a, b in vertex:
        g[a].add(b)
        g[b].add(a)
    return g


def solution(n, edge):
    g = graph(edge, n)
    visited = [(1, 0)]
    queue = deque([(1, 0)])
    while queue:
        p = queue.popleft()
        neighbor = g[p[0]] - set(visited)
        for i in neighbor:
            if i not in [x for x, y in visited]:
                queue.append((i, p[1] + 1))
                visited.append((i, p[1] + 1))
    answer = 0
    for visit in visited:
        if visit[1] == visited[-1][1]:
            answer += 1
    return answer


test_n = 6
test_vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# graph(test_vertex, test_n)
print(solution(test_n, test_vertex))