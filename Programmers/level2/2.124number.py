# 3:07

def solution(n):
    answer = ''
    num_list = ['4', '1', '2']
    while n > 0:
        answer = num_list[n%3] + answer
        n = (n-1)//3

    return answer


print(solution(27))