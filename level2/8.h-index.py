def solution(citations):
    answer = 0
    for n in range(1, len(citations) + 1):
        more = [c for c in citations if c>=n]
        if len(more) >= n:
            answer += 1

    return answer



citations = [3, 0, 6, 1, 5]
citations = [3,3,3]
ans = solution(citations)
print(ans)