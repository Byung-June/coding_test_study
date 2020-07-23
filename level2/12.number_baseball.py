# 10:11

def checker(sample, num):
    s, b = 0 , 0
    m = list(str(sample))
    n = list(str(num))
    # print(m, n)
    for i, j in enumerate(m):
        if j == n[i]:
            s+=1
    for i in set(m):
        if i in set(n):
            b +=1

    return [s, b-s]


def solution(baseball):
    candidate = []
    for i in range(111, 1000):
        if '0' in list(str(i)):
            continue
        if len(set(str(i))) == 3:
            c = True
            for sample_list in baseball:
                s, b = checker(i, sample_list[0])
                if s != sample_list[1]:
                    c = False
                    break
                if b != sample_list[2]:
                    c = False
                    break
            # print(i, c)
            if c:
                candidate.append(i)

    # print('can', candidate)
    answer = len(candidate)
    return answer


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
ans = solution(baseball)
print(ans)

sample = 548
num = 125
print(checker(sample, num))

i = 322
print(list(str(i)))
print(len(set(str(i))))