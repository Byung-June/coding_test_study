# 12:24 ~
def DFS_with_adj_list(computers, root):
    visited = []
    stack = [root]

    while stack:
        k = stack.pop()
        if k not in visited:
            visited.append(k)
            check = [j for i, j in enumerate(computers[k]) if i!=k]
            if 1 in check:
                temp = list(set([i for i, j in enumerate(computers[k]) if j == 1]) - set(visited))
                stack += temp

    return visited


def solution(n, computers):
    answer = 0
    stack = []
    for i in range(n):
        if not any(i in cycle for cycle in stack):
            stack.append(DFS_with_adj_list(computers, i, n))
            answer += 1

    return answer

def solution2(n, computers):
    stack = [i for i in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            print('num',i, j, computers[i][j])
            if computers[i][j] == 1:
                print(stack[j], stack[i], stack)
                stack = [stack[i] if k == stack[j] else k for k in stack]
                print(stack)
    print('stack', stack, set(stack))
    answer = len(set(stack))
    return answer


n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

# n = 4
# computers =  [[1,0,0,1],[0,1,1,1],[0,1,1,0],[1,1,0,1]]
# print('!!', DFS_with_adj_list(computers, 0, 3))

print(solution2(n, computers))

from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited