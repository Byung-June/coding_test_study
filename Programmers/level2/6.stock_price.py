# 12:39

def solution0(prices):
    answer = []
    for i, p in enumerate(prices[:-1]):
        p_val = 0
        for j, pp in enumerate(prices[i+1:]):
            p_val += 1
            if pp >= p:
                if j == len(prices[i+1:])-1:
                    answer.append(p_val)
                    break
            else:
                answer.append(p_val)
                break

    answer.append(0)
    return answer

def solution(prices):
    answer = []
    for i, p in enumerate(prices[:-1]):
        p_val = 0
        for j in range(i+1, len(prices)):
            p_val += 1
            if p > prices[j]:
                answer.append(p_val)
                break
            else:
                if j == len(prices)-1:
                    answer.append(p_val)
                    break
    answer.append(0)
    return answer

# prices = [1, 2, 3, 2, 3]
prices = [3, 3, 1, 10, 20]
ans = solution(prices)
print(ans)