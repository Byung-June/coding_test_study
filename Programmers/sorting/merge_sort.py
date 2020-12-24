nums = [5,2,31,2,5,7, 9, 10]


def merge(a, b):
    c = []  # final return
    a_ind, b_ind = 0, 0

    while a_ind<len(a) and b_ind<len(b):
        if a[a_ind] < b[b_ind]:
            c.append(a[a_ind])
            a_ind +=1
        else:
            c.append(b[b_ind])
            b_ind +=1
    if a_ind==len(a): c.extend(b[b_ind:])
    else: c.extend(a[a_ind:])
    return c


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    left, right = merge_sort(nums[:len(nums)//2]), merge_sort(nums[len(nums)//2:])
    return merge(left, right)


print(merge_sort(nums))
