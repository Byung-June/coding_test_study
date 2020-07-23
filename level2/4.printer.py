# 9:25 ~ 9:41

def solution(priorities, location):
    answer = 0
    while True:
        print(priorities, location, answer)
        if priorities[0] == max(priorities):
            if location == 0:
                answer += 1
                break
            else:
                location -= 1
                priorities.pop(0)
                answer += 1
        else:
            if location == 0:
                location += len(priorities) - 1
                priorities.append(priorities[0])
                priorities.pop(0)
            else:
                location -= 1
                priorities.append(priorities[0])
                priorities.pop(0)

    return answer

# prio = [1, 1, 9, 1, 1, 1]
prio = [2, 1, 3, 2]
ans = solution(prio, 2)
print(ans)