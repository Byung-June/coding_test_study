def str_to_interval(line):
    line = line.split()
    end = line[1].split(':')
    end = int(end[0]) * 3600 * 1000 + int(end[1]) * 60 * 1000 + int(float(end[2]) * 1000)
    start = line[2][:-1]
    start = end - int((float(start)) * 1000)
    end += 999
    return [start, end]


def check_in_interval(time, interval_list):
    num = 0
    # print('time', time)
    for interval in interval_list:
        if (time >= interval[0]) and (time < interval[1]):
            num += 1
            # print('int', interval)
    return num


def solution(lines):
    answer = 0
    lines = [str_to_interval(line) for line in lines]
    lines.sort(key=lambda x: (x[0], x[1]))
    # print(lines)
    for line in lines:
        a = check_in_interval(line[0], lines)
        if a > answer:
            answer = a

    return answer


test = [
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]
print(solution(test))

test = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(test))

test = [
'2016-09-15 01:00:04.002 2.0s',
'2016-09-15 01:00:07.000 2s'
]
print(solution(test))