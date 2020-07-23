# 1:47 ~


def gen(x):
    return [0 if i%2 == 0 else 1 for i in range(int(2 ** (x-1)))]


def solution(n):
    answer = []
    before = []
    gener = gen(n)
    if n > 0:
        before = list(solution(n-1))
    # print('before', before, 'gen', gen(n))

    for i in range(int(2 ** n - 1)):
        if i % 2 == 0:
            answer.append(gener[i//2])
        else:
            answer.append(before[(i-1)//2])

    return answer


def solution2(n):
    answer = [0]
    for i in range(1,n):
        k = [1-j for j in answer]
        answer = answer + [0] + k[::-1]

    return answer


# print([i for i in range(1)])
n = 3
print(solution(n))