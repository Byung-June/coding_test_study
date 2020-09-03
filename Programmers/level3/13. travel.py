def bfs_adj(graph, root, tickets):
    stack = [root]
    visited =[]
    while tickets:
        n = stack.pop()
        # print('n',n, stack, visited)
        if n in tickets:
            try:
                stack.extend(graph[n[1]])
                tickets.remove(n)
                visited.append(n)
            except KeyError:
                if len(tickets) <= 1:
                    visited.append(n)
                    break
                stack.insert(0, n)
        # print('stack', stack)
    return visited


def solution(tickets):
    answer = []
    book = {}
    for key in tickets:
        if key[0] in book.keys():
            book[key[0]].append(key)
        else:
            book[key[0]] = [key]
    for key in book.keys():
        book[key] = sorted(book[key], reverse=True)
    # print('book', book)
    first = 'ICN'
    visited = bfs_adj(book, book[first][-1], tickets)
    # print('visited', visited)
    for place in visited:
        answer.append(place[0])
    answer.append(visited[-1][-1])
    return answer


tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND'], ['JFK', 'ICN'], ['ICN', 'JFK']]
# tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
print(solution(tickets))