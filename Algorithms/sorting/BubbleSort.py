"""for bubble sort we take the maximum and push it At the end of the array"""

def bubble_sort(nums):

    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:

                ## SWAP
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums



print(bubble_sort([4,2,6,-5,1,3]))