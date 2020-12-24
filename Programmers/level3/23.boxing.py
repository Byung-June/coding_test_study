def solution(n, results):
    d = [[0] * n for _ in range(n)]

    for i, j in results:
        d[i - 1][j - 1] = 1
        d[j - 1][i - 1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] == 0:
                    if d[i][k] == 1 and d[k][j] == 1:
                        d[i][j] = 1
                    if d[i][k] == -1 and d[k][j] == -1:
                        d[i][j] = -1

    answer = 0
    for win_lose in d:
        if win_lose.count(0) == 1:
            answer +=1
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
