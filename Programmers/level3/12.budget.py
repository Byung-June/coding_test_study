def solution(budgets, M):

    if sum(budgets) <= M:
        return max(budgets)
    else:
        lb = 0
        ub = M
        while True:
            answer = (lb + ub)//2
            result_budgets = [min(i, answer) for i in budgets]
            if sum(result_budgets) <= M:
                lb = answer
            else:
                ub = answer
            if lb + 1 >= ub:
                if sum([min(i, ub) for i in budgets]) <= M:
                    answer = ub
                else:
                    answer = lb
                break
        return answer



budgets = [119, 110, 140, 150]
M = 485
ans = solution(budgets, M)
print(ans)