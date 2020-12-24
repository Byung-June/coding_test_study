from collections import deque

def gen_graph(tickets):
    graph = {start: [] for start in [i[0] for i in tickets]}
    pass_num = {}
    for start, arrive in tickets:
        graph[start].append(arrive)
        if start in pass_num.keys():
            pass_num[start] += 1
        else:
            pass_num[start] = 1
        if arrive in pass_num.keys():
            pass_num[arrive] += 1
        else:
            pass_num[arrive] = 1
    for start, arrive in tickets:
        graph[start] = sorted(graph[start], reverse=True)
    for city, num in pass_num.items():
        if (num % 2 == 1) and (num != "ICN"):
            pass_num = city
    return graph, pass_num


def solution(tickets):
    graph, last = gen_graph(tickets)
    print('graph: ', graph, 'last', last)
    path = ["ICN"]
    while len(path) != len(tickets) + 1:
        city = path[-1]
        possible = graph[city]

        if len(path) < len(tickets) and possible[-1] not in graph.keys():
            back = 1
            while possible[-back] not in graph.keys():
                back += 1
            next_city = graph[city].pop(-back)
        else:
            next_city = graph[city].pop()
        path.append(next_city)

        if len(path) == len(tickets) + 1:
            return path


# test_tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
# print(solution(test_tickets))
#
# test_tickets = [['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]
# print(solution(test_tickets))

test_tickets = [['ICN','BOO'], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
print(solution(test_tickets))
