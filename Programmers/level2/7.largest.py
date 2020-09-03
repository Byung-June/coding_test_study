def solution(numbers):
    answer = ''
    str_list = [str(n) for n in numbers if n != 1000 if n != 100 if n != 0]
    str_list = sorted(str_list, key=lambda x: int((str(x) * 4)[:3]), reverse=True)

    ze_list0 = ['100'] * numbers.count(100)
    ze_list1 = ['1000'] * numbers.count(1000)
    ze_list2 = ['0'] * numbers.count(0)
    # print(ze_list0, ze_list1, ze_list2)
    str_list.extend(ze_list0)
    str_list.extend(ze_list1)
    str_list.extend(ze_list2)

    for elt in str_list:
        if answer == '0' and elt=='0':
            answer = '0'
        else:
            answer += elt
    print(str_list)
    return answer



numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9, 333, 346, 347, 340, 4, 0, 1000, 81, 989, 992, 1, 57, 578, 571, 0, 1000, 100, 0]
# numbers = [0, 1000, 100, 0]

ans = solution(numbers)
print(ans)