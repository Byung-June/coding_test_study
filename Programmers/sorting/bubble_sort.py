nums = [5,2,31,2,5,7, 9, 10]

def bubble_sort(nums):

    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    return nums

bubble_sort(nums)