from itertools import permutations
import math

def prime_check(num):
    ans = True
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    r = math.floor(num ** 0.5)
    for trial in range(3, r + 1, 2):
        if num % trial == 0:
            return False

    return ans


def solution(numbers):
    prime = []
    for i in range(1, len(numbers)+1):
        nn = permutations(numbers, i)
        for n in nn:
            made = int(''.join(list(n)))
            if made not in prime:
                if prime_check(made):
                    prime.append(made)
    answer = len(prime)
    return answer

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


numbers = "123425"
ans = solution(numbers)
print(ans)
#
# n = 49
# print(prime_check(n))