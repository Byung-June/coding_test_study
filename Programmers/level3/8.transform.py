
def spell_check(s1, s2):
    ans = [1 for i in range(len(s1)) if s1[i] != s2[i]]
    return sum(ans)


def solution(begin, target, words):
    answer = 0
    book = {}
    words = [begin] + words

    visited = [False] * len(words)


    for i in words:
        val = []
        for j in words:
            if spell_check(i, j) == 1:
                val.append(j)
        book[i] = val

    arrived = False
    visited = []
    parents = {}
    queue = [begin]

    while queue:
        n = queue.pop(0)
        if n == target:
            visited.append(n)
            arrived = True
            break
        if n not in visited:
            visited.append(n)
            temp = list(set(book[n]) - set(visited))
            queue += temp
            for k in temp:
                if k not in parents.keys():
                    parents[k] = n

    if arrived == True:
        path = [target]
        while path[-1] != begin:
            path.append(parents[path[-1]])
            # print(path)
        answer = len(path) -1
    return answer


begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

ans = solution(begin, target, words)
print(ans)