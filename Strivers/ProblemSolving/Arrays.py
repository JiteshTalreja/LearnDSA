#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q1 Find the largest number in an unsorted Array


## solution Brute force to sort the array.

## Optimal solution is below

def largest(nums):

    maxi = nums[0]

    for i in nums:
        if i > maxi:
            maxi = i
    return maxi
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

## Q2 second largest in a unsorted array

## AGAIN Brute force is to sort the array

## BETTER

def slargest(nums):

    ## First find the largest
    largest = nums[0]

    for i in nums:
        if i > largest:
            largest = i
    slargest = -1

    for i in nums:
        if i > slargest and i != largest:
            slargest = i
    return slargest

print(slargest([3,20,10,15,2]))

## OPTIMAL SOLUTION

def sslargest_opt(nums):

    largest = nums[0]
    slargest = -1

    for i in nums:
        if i > largest:
            slargest = largest
            largest = i

        elif i < largest and i > slargest:
            slargest = i

    return slargest

print('slarge opt', sslargest_opt([3,20,10,15,2]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q3 Check if list is sorted

def is_sorted(nums):
    for i, v in enumerate(nums):
        if v> nums[i+1]:
            return False
    return True

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q4 Remove duplicates from an array

def remove_dups(nums):
    i = 0
    j =1

    while j < len(nums):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]
        j+=1
    return nums[:i+1]

print(remove_dups([1,1,1,2,2,2,3,3,3,4,4,4]))