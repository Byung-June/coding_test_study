def solution(clothes):
    if len(clothes)==0:
        return 0
    else:
        book = {}
        for i,j in clothes:
            if j in book.keys():
                book[j].append(i)
            else:
                book[j] = [i]
        print(book)

        ll = 1
        for key in book.keys():
            ll *= len(book[key]) + 1

        answer = ll - 1

        return answer

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
ans = solution(clothes)
print(ans)

