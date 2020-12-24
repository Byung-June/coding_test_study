import math


def proceed(progresses, speeds, num):
    return [a + b * num for a, b in zip(progresses, speeds)]


def solution(progresses, speeds):
    answer = []

    while len(progresses) > 0:
        a = 0
        if progresses[0] < 100:
            num = math.ceil((100-progresses[0])/speeds[0])
            progresses = proceed(progresses, speeds, num)
        else:
            while progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                a += 1
                if len(progresses) == 0:
                    break
            answer.append(a)
    return answer


a = [93, 30, 55]
b= [1, 30, 5]
sol = solution(a, b)
print(sol)