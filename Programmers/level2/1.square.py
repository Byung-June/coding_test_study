def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


def solution(w,h):
    g = gcd(w, h)
    a = max(w//g, h//g)
    b = min(w//g, h//g)
    print(g, a,b, a//b)
    if a !=b:
        answer = w * h - g * (a+b-1)
    else:
        answer = w * h - g
    return answer

print(solution(5, 8))