def count(t, times):
    return sum([t//time for time in times])


def solution(n, times):
    times.sort()
    left = 0
    right = n * times[0]
    mid = (left+right) // 2

    while left <= right:
        mid = (left + right) // 2
        test = count(mid, times)
        if test >= n:
            right = mid - 1
        elif test < n:
            left = mid + 1
    return mid

n = 6
times = [7, 10]
print(solution(n, times))