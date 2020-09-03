def solution(n):
    if n <3:
        return n
    else:
        f = []
        f.append(1)
        f.append(2)
        for i in range(2, n):
            f.append((f[-1] + f[-2]) % 1000000007)
        return f[-1]

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(40))
