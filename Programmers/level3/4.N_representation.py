# 10:41 ~

def list_com(a, b):
    c = []
    for i in a:
        for j in b:
            c.append(i + j)
            if i > j:
                c.append(i - j)
            else:
                c.append(j - i)
            c.append(i * j)
            if j != 0:
                c.append(i//j)
            if i != 0:
                c.append(j // i)
    c = list(set(c))
    # print('comp', a, b, c)
    return c

def solution(N, number):
    answer = 0
    space = [[N]]

    for i in range(1, 9):
        if number in space[i-1]:
            # print('number!!', number, space[i-1])
            answer = i
            break
        else:
            new = []
            for j in range(i//2 + 1):
                # print(i, j)
                # print(list_com(space[j], space[i-1-j]))
                new.extend(list_com(space[j], space[i-j-1]))
            new.append(int('1' * (i+1)) * N)
            space.append(new)
            # print(i, space)

    if answer ==0:
        answer = -1

    return answer


N = 4
number = 17
print(solution(N, number))
