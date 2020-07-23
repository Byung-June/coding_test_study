# 9:15 ~ 9:24

def solution(heights):
    answer = []
    for i, top in enumerate(heights):
        while True:
            if i < 1:
                answer.append(0)
                break
            if heights[i-1] > top:
                answer.append(i)
                break
            else:
                i -= 1

    return answer



# height = [6,9,5,7,4]
height = [3,9,9,3,5,7,2]
ans = solution(height)
print(ans)
