def binary_search(arr, val):
    start, end = 0, len(arr)
    print(start, end)
    while start <= end:

        pos = (start + end) // 2
        print(start, end, pos)
        if arr[pos] == val:
            return pos
        if arr[pos] > val:
            end = pos - 1
        else:
            start = pos + 1


import numpy as np



if __name__=='__main__':
    arr = range(2, 100, 2)
    print(arr)
    bin = binary_search(arr, 30)
    print(bin)

