def solution(a, b):
    answer = ''
    end_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for mon, date in enumerate(end_list):
        if mon < 12:
            end_list[mon+1] += date
    num = (end_list[a-1] + (b-1)) % 7
    day_string = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    answer = day_string[num]


    return answer



print(solution(5, 24))