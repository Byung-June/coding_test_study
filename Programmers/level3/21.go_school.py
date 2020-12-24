def solution(m, n, puddles):
    if (m == 1 or n == 1) and len(puddles) > 0:
        return 0

    S = [[1] * n for _ in range(m)]

    for i, j in puddles:
        S[i - 1][j - 1] = 0
        if i-1 == 0:
            for k in range(j-1, n):
                S[0][k] = 0
        elif j-1 == 0:
            for k in range(i-1, m):
                S[k][0] = 0
        else:
            pass

    for i in range(1, m):
        for j in range(1, n):
            if S[i][j] != 0:
                S[i][j] = S[i-1][j] + S[i][j-1]

    return S[m-1][n-1] % 1000000007


m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))