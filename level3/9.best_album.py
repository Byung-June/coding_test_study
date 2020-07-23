# 2: 38

def solution(genres, plays):
    answer = []
    tot = {}
    gen_num = {}

    for i, j, n in zip(genres, plays, range(len(genres))):
        if i in tot.keys():
            tot[i] += j
            gen_num[i].append(n)
        else:
            tot[i] = j
            gen_num[i] = [n]

    for gen, val in sorted(tot.items(), key=lambda x: x[1], reverse=True):
        re = sorted(gen_num[gen], key=lambda x: plays[x], reverse=True)[:2]
        answer.extend(re)
        # print(gen, re)

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'k']
plays = [500, 600, 150, 800, 2500, 1]
ans = solution(genres, plays)
print(ans)

