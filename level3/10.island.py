def solution(n, costs):
    book = {}
    for i in costs:
        if i[0] in book.keys():
            book[i[0]].append([i[1], i[2]])
        else:
            book[i[0]] = [[i[1], i[2]]]
        if i[1] in book.keys():
            book[i[1]].append([i[0], i[2]])
        else:
            book[i[1]] = [[i[0], i[2]]]
    # print('book', book)

    cost = []
    visited = [0]
    while len(visited) < n:
        adj_list = []
        for i in visited:
            # print('for', i, book[i], visited)
            adj = [j for j in book[i] if j[0] not in visited if j not in adj_list]
            adj_list.extend(adj)
        # print('adj list', adj_list)
        m = min(adj_list, key=lambda x: x[1])
        visited.append(m[0])
        cost.append(m[1])
    # print(visited, cost)
    answer = sum(cost)
    return answer




n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
ans = solution(n, costs)
print(ans)

