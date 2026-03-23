def insertion_sort(nums):

    for i in range(1, len(nums)):

        key = nums[i]
        j = i-1

        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            nums[j] = key
            j-=1
    return nums


print(insertion_sort([4,2,6,5,1,3]))