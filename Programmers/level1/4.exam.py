def solution(answers):
    answer = []
    num = [0,0,0]
    second = [1,3,4,5]
    third = [3,1,2,4,5]
    for i, j in enumerate(answers):
        # print(i, j)
        if i % 5 == j-1:
            num[0] += 1
        if i % 2 == 0:
            if j == 2:
                num[1] += 1
        else:
            # print((i//2) % 5)
            if j == second[(i//2) % 4]:
                num[1] += 1
        if third[(i//2)%5] == j:
            num[2] +=1
        # print(num)

    for order, val in enumerate(num):
        if val == max(num):
            answer.append(order+1)

    return answer


# answers = [1,2,3,4,5, 5, 2]
# answers = [1, 3, 2, 4, 2]
# answers = [2, 1, 2, 3, 2, 4, 2]
answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4]
ans = solution(answers)
print(ans)