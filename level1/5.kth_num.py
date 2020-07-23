def solution(array, commands):
    answer = []
    for i,j,k in commands:
        elt = array[i-1:j]
        elt = sorted(elt)[k-1]
        answer.append(elt)
    return answer


def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


arr = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
ans = solution(arr, command)