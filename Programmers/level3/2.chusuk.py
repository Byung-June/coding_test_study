# 3:56 ~
import time

def solution(lines):
    answer = 0
    start = []
    end = []
    count = []
    for str in lines:
        _, time, period = str.split()
        hh = int(time[0:2])
        mm = int(time[3:5])
        ss = int(time[6:8])
        ms = float('0.' + time[9:])
        print(hh, mm, ss, ms, ms * 1000)
        start.append((hh * 60 * 60 + mm * 60 + ss) * 1000 + int(ms * 1000))
        end.append(int(1000 * float(period[:-1])))
    print(start, end)
    book = [[a, a + b + 999] for a, b in zip(start, end)]
    book = sorted(book, key=lambda x: (x[0], x[1]))
    print(book)
    for t in range(len(lines)):
        num = 1
        for i in range(t):
            print(t, i)
            # print('check', t, i, book[i][1], book[t][0], book[i][1] > book[t][0], type(book[i][1]), type(book[t][0]))
            if book[i][1] > book[t][0]:
                num += 1
                print(t, i)
        count.append(num)
    print(count)
    answer = max(count)
    return answer


lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
# lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))
# print([i for i in lines[0:1]])