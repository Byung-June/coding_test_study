from functools import reduce


def num_digits(nums):
    m = nums[0]
    for item in nums:
        if item > m:
            m = item
    return len(str(m))


def flatten(box):
    return reduce(lambda x, y: x+y, box)


def radix_sort(nums):
    for digits in range(num_digits(nums)):
        box = [[] for i in range(10)]
        for item in nums:
            num = item // (10 ** digits) % 10
            box[num].append(item)
        nums = flatten(box)

    return nums


print(radix_sort(nums=[511, 2, 331, 2, 51, 7, 95, 110]))
