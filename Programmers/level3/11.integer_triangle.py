def solution(triangle):
    value = triangle[::-1]
    for n in range(1, len(triangle)):
        for m in range(len(triangle) - n):
            value[n][m] = max(value[n][m] + value[n-1][m], value[n][m] + value[n-1][m+1])
    # print(value)
    answer = value[-1][0]
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))

