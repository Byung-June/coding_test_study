nums = [5,2,31,2,5,7, 9, 10]

def quick_sort(nums):

    if len(nums) <= 1: return nums
    smaller, equal, larger = [], [], []
    pivot = nums[0]

    for x in nums:
        if x < pivot: smaller.append(x)
        elif x == pivot: equal.append(x)
        else: larger.append(x)

    return quick_sort(smaller) + equal + quick_sort(larger)

print(quick_sort(nums))
