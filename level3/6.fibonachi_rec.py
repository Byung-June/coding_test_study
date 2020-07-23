def solution(N):
    if N == 1:
        answer = 4
    elif N==2:
        answer = 6
    else:
        fib = [1, 1]
        for i in range(2, N):
            fib.append(fib[-1]+fib[-2])
        answer = fib[-1] * 4 + fib[-2] * 2
    return answer


N = 6
print(solution(N))