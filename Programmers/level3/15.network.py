from collections import deque

def graph(matrix):
    graph = {com: set() for com in range(len(matrix))}
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if (col == 1) and i!=j:
                graph[i].add(j)
    return graph


def solution(n, computers):
    visited = []
    computers = graph(computers)
    answer = 0

    for i in range(n):
        if i in visited:
            continue
        queque = deque([i])
        while queque:
            k = queque.popleft()
            if k not in visited:
                visited.append(k)
                queque += computers[k] - set(visited)
        answer +=1

    return answer

test1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(3, test1))