def solution(n, lost, reserve):
    answer = n

    for s in lost:
        if s in reserve:
            reserve.remove(s)
        elif s-1 in reserve:
            reserve.remove(s-1)
        elif s+1 in reserve:
            if s+1 in lost:
                answer -= 1
            else:
                reserve.remove(s+1)
        else:
            answer -= 1

    return answer






n = 10
lost = [2,4, 6, 7]
reserve = [1,3,5, 8]

ans = solution(n, lost, reserve)
print(ans)