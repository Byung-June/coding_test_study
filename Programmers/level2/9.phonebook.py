def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    for num in range(len(phone_book)):
        for com in range(num+1, len(phone_book)):
            lenght = len(phone_book[num])
            print(phone_book[com][:lenght],phone_book[num])
            if phone_book[com][:lenght] == phone_book[num]:
                return False

    return answer


phone_book = ['97674223', '1195524421', '119']
ans = solution(phone_book)
print(ans)