def solution(numbers, target):
    n = numbers[0]
    m = len(numbers)
    c = int((n * m - target) /2)

    fact = [1, 1]
    for i in range(2, m+1):
        fact.append(fact[-1] * i)
    # print(fact, m, c, m-c)
    answer = fact[m] / fact[c] / fact[m-c]

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
