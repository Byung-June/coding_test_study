def solution(participant, completion):
    answer = ''
    book_com = dict()
    for i in completion:
        if i not in book_com:
            book_com[i] = 1
        else:
            book_com[i] += 1
    # print(book)

    book_par = dict()
    for j in participant:
        if j not in book_com:
            answer = j

        else:
            if j in book_par:
                book_par[j] += 1
            else:
                book_par[j] = 1
    # print(book_par)

    if len(answer) == 0 :
        for k in book_par.keys():
            if book_com[k] < book_par[k]:
                answer = k

    return answer





if __name__=='__main__':
    part = ["mislav", "stanko", "mislav", "ana"]
    com = ["stanko", "ana", "mislav"]
    #
    # part = ["leo", "kiki", "eden"]
    # com = ["eden", "kiki"]

    ans = solution(part, com)
    print(ans)

    # dict1 = {'mislav': 465142561288692516000002, 'stanko': -82124417100449895899999, 'ana': 258229247135264830300001}
    # print('mislav' not in dict1)
