import math

def solution(brown, yellow):
    term = math.sqrt((brown+4)**2 /4 - 4 * (brown + yellow))
    w = ((brown + 4) / 2 + term) / 2
    h = ((brown + 4) / 2 - term) / 2
    return [w,h]

brown = 10
yellow = 2
ans = solution(brown, yellow)
print(ans)