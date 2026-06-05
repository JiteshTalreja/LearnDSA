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

# print(slargest([3,20,10,15,2]))

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

# print('slarge opt', sslargest_opt([3,20,10,15,2]))

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

# print(remove_dups([1,1,1,2,2,2,3,3,3,4,4,4]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------LEFT ROTATE-------------------------------------------------------------------------------------------------
## Q5 Rotate an array by k places
## Right rotate by k = Left rotate by (n - k)

def left_rotate(nums, k):
    return nums[k:] + nums[:k]

# print(left_rotate([1,2,3,4,5,6,7], 3))

# another method

def left_rotate2(nums, k):
    k%=len(nums)
    n = len(nums)
    l2 = []
    for i in range(k):
        l2.append(nums[i])

    for i in range(k, n):
        nums[i-k] = nums[i]

    for i in range(n-k, n):
        nums[i] = l2[i-(n-k)]
    return nums
print("left_rotate2", left_rotate2([1,2,3,4,5,6,7], 3))

## best and Optimal solution for this is using reverse:
## Reverse first k
## reverse last n-k
## reverse full list


#------------------------------------------------RIGHT ROTATE------------------------------------------------------------------------------------------------


def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        r-=1
        l+=1

def right_rotate(nums, k):
    k %= len(nums)

    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    return nums
print(right_rotate([1,2,3,4,5,6,7], 3))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q6 Move all zeros at the end of an array

list1  = [1,0,2,3,2,0,0,4,5,1]

## [1,2,0,3,2,0,0,4,5,1]

def push_back(nums, item=0):
    i = 0
    j = 1

    while j<=len(nums)-1:
        print(j)
        if nums[i]==item and nums[j]!=item:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j+=1
        elif nums[i] != item:
            i+=1
            j+=1
        else:
            j+=1

    return nums

print(push_back(list1))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q7 Union  of 2 arrays:

## Brute
def union(l1, l2):
    set1 = set()

    for i in l1:
        set1.add(i)
    for j in l2:
        set1.add(j)
    return set1

print(union([1,1,2,3,4,5,], [2,3,4,4,5,6]))

## OPTIMAL
def union_sorted(l1, l2):
    i = j = 0
    res = []

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            if not res or res[-1] != l1[i]:
                res.append(l1[i])
            i += 1
        else:
            if not res or res[-1] != l2[j]:
                res.append(l2[j])
            j += 1

    while i < len(l1):
        if not res or res[-1] != l1[i]:
            res.append(l1[i])
        i += 1

    while j < len(l2):
        if not res or res[-1] != l2[j]:
            res.append(l2[j])
        j += 1

    return res

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q7 Intersection of 2 arrays:

##BRUTE
def intersection_with_duplicates(l1, l2):
    res = []
    used = [False] * len(l2)

    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j] and not used[j]:
                res.append(l1[i])
                used[j] = True
                break

    return res

## OPTIMAL

def intersection_sorted(l1, l2):
    l1.sort()
    l2.sort()

    i = j = 0
    res = []

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            res.append(l1[i])
            i += 1
            j += 1

    return res


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q8 Find missing number in array

##Brute
def missing_brute(nums, n):

    for i in range(1, n):
        flag = False
        for j in range(0, n-1):
            if nums[j] == i:
                flag = True
                break
        if not flag:
            return i

print(missing_brute([1,2,4,5], 5))


## Better
def missing_better(nums, n):
    hash = [0]*(n+1)

    for i in nums:
        hash[i] = 1

    for i in range(1, n):
        if hash[i] == 0:
            return i

print(missing_better([1,2,4,5], 5))


## Optimal
def missing_optimal(nums, n):
    sum_n = int((n*(n+1))/2)
    cur_sum = 0
    for i in nums:
        cur_sum+=i

    return sum_n - cur_sum
print(missing_optimal([1,2,4,5], 5))

## Optimal 2
def missing_optimal2(nums, n):
    xor1 = 0
    xor2 = 0
    for i in range(0, n-1):
        xor1 ^= i+1
        xor2 ^= nums[i]
    xor1^=n
    return xor1^xor2

print(missing_optimal2([1,2,4,5,], 5))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q9 Find maximum consecutive 1s

def max_con_1(nums):
    maxi = 0
    counter = 0
    for i in nums:
        if i ==1:
            counter+=1
            maxi = max(maxi, counter)
        else:
            counter = 0
    return maxi
# print(max_con_1([1,1,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q9 Find the number that just appears once in an array

##Brute
def single_number_brute(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count == 1:
            return nums[i]

## Better
def single_number_better(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num in nums:
        if freq[num] == 1:
            return num

## Optimal
def single_number_optimal(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q10 Find Longest Subarray with Sum - k

##Brute

def long_brute(nums, k):
    n = len(nums)
    longest = 0

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                longest = max(longest, j - i + 1)
    return longest

print('long: ', long_brute([1,2,3,1,1,1,1,4,5,2], 3))

## Optimal (USING PrefixSum)
"""
In python since we are using dict this is O(n), for C++ Striver was using ordered map which has search complexity of Logn
"""


def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    max_len = 0
    mp = {}  # prefix_sum -> first index

    for i in range(len(nums)):
        prefix_sum += nums[i]

        # Case 1: subarray from 0 to i
        if prefix_sum == k:
            max_len = i + 1

        # Case 2: subarray in between
        if (prefix_sum - k) in mp:
            length = i - mp[prefix_sum - k]
            max_len = max(max_len, length)

        # Store only FIRST occurrence
        if prefix_sum not in mp:
            mp[prefix_sum] = i

    return max_len
print("long optimal:", longest_subarray_sum_k([1, 0, 2, 0, 1], 3))


## Optimal using 2 pointer

def longest_subarray_sum_k_optimal2(nums, k):
    i = 0
    j = 0
    total = 0
    maxi = 0

    while j < len(nums):
        total += nums[j]

        while total > k:
            total -= nums[i]
            i += 1

        if total == k:
            maxi = max(maxi, j - i + 1)

        j += 1

    return maxi

print("long optimal2:", longest_subarray_sum_k_optimal2([1, 0, 2, 0, 1], 3))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q11 2 sum

## Brute

def two_sum_brute(nums, target):
    n = len(nums)
    l2 = []
    for i in range(n):
        for j in range(i+1, n):
            sum2 = nums[i]+nums[j]
            if sum2 == target:
                l2.append([i, j])
    return l2

print(two_sum_brute([2,6,5,8,11], 14))


## Better

def two_sum_better(nums, target):
    hash = {}
    l3 = []

    for i, v  in enumerate(nums):
        if target - v in hash:
            l3.append([i, hash[target-v]])
        hash[v] = i
    return l3
print(two_sum_better([2,6,5,8,11], 14))

##Optimal

def two_sum_optimal(nums, target):
    nums.sort()
    i = 0
    j = len(nums)-1
    l3 = []

    while i < j:
        sum = nums[i] + nums[j]

        if sum == target:
            l3.append([i,j])
            i+=1
            j-=1
        elif sum < target:
            i += 1
        else:
            j -= 1
    return l3

print('2sum_opt', two_sum_optimal([2,6,5,8,11, 3], 14))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q12 Sort an array of 0's 1's & 2's

## BRUTE
def sort_colors_brute(nums):
    nums.sort()
    return nums

### BETTER
def sort_colors_better(nums):
    count0 = count1 = count2 = 0

    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    i = 0

    for _ in range(count0):
        nums[i] = 0
        i += 1
    for _ in range(count1):
        nums[i] = 1
        i += 1
    for _ in range(count2):
        nums[i] = 2
        i += 1

    return nums

## OPTIMAL (Using Dutch National flag)

def sort_colors_optimal(nums):
    low = 0
    mid =0
    high = len(nums)-1

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low +=1
            mid+=1

        elif nums[mid] == 1:
            mid+=1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high-=1
    return nums


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q13 Majority Element (find an element from a given array which appear more than n//2 times)

## Brute

def major_brute(nums):

    for i in nums:
        count=0
        for j in nums:
            if j == i:
                count+=1
        if count > len(nums)//2:
            return i


print('major brute', major_brute([2,2,3,4,2,4,2,2,2,4,5,2]))


## Better (using hash map)

def major_better(nums):
    mp = {}

    for i in nums:
        mp[i] =mp.get(i, 0)+1

        if mp[i] > len(nums)//2:
            return i
    return None

print('major better', major_better([2,2,3,4,2,4,2,2,2,4,5,2]))

## optimal (using Moore's Voting Algorithm)

def major_optimal(nums):
    count = 0
    candidate = 0

    for num in nums:
        if count ==0:
            candidate = num

        if num == candidate:
            count+=1
        else:
            count-=1
        # verification step
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None
print('major optimal', major_optimal([2,2,3,4,2,4,2,2,2,4,5,2]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q14 Kadane's Algorithm (Maximum subarray sum)

## Max Sum
def max_subarray_sum(nums):
    current_sum = 0
    max_sum = float('-inf')

    for num in nums:
        current_sum +=num

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum=0
    return max_sum

print("kadane's sum", max_subarray_sum([-3, -2, -5]))

## Subarray for max sum
def max_subarray(nums):
    max_sum = float('-inf')
    current_sum = 0

    start = end = temp_start = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        # update answer
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        # reset if bad
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return nums[start:end+1], max_sum

print("kadane's sub array", max_subarray([-3, -2, -5]))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q15 Best Time to Buy and Sell Stock

"""
prices = [7,1,2,4,6,5,8,2,9]
"""

def stocks(prices):
    mini = prices[0]
    profit = 0

    for price in prices:
        mini = min(mini, price)              # best buy so far
        profit = max(profit, price - mini)   # best sell

    return profit

print("profit: ", stocks([7,1,2,4,6,20,8,2,19]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q16 Rearrange array elements by the sign

## Brute ( Time Complexity: O(n) + O(n), Space Complexity O(n)
def arrange_brute(nums):
    pos = []
    neg = []
    for i in nums:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)

    for i in range(len(nums)//2):
        nums[2*i] = pos[i]
        nums[2*i+1] = neg[i]
    return nums

print("arrange brute :", arrange_brute([3,1,-2,-5,2,-4]))


## optimal

def arrange_optimal(nums):
    n = len(nums)
    res = [0]*n
    pos = 0
    neg = 1

    for num in nums:
        if num > 0:
            res[pos] = num
            pos +=2
        else:
            res[neg] = num
            neg +=2
    return res

print("arrange optimal :", arrange_optimal([3,1,-2,-5,2,-4]))

## Variation: When unequal number of elements are present

## nums: [-1,2,3,4,-3,1]

def rearrange_variation(nums):
    pos = [x for x in nums if x >= 0]
    neg = [x for x in nums if x < 0]

    res = []
    i = j = 0

    # alternate
    while i < len(pos) and j < len(neg):
        res.append(pos[i]); i += 1
        res.append(neg[j]); j += 1

    # remaining elements
    res.extend(pos[i:])
    res.extend(neg[j:])

    return res

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q17 Given an array nums of distinct integers, return next permutations. (similar questions Asked in Nike round)


def next_permutation(nums):

    n= len(nums)

    i = n-2


    #pivot point
    while i >=0 and nums[i] >= nums[i+1]:
        i-=1

    # next greatest

    if i>=0:

        j = n-1

        while nums[j] <= nums[i]:
            j-=1

        nums[j], nums[i] = nums[i], nums[j]

    left = i+1
    right = n-1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left+=1
        right-=1
    return nums
print("next permutation: ",next_permutation([2,1,5,4,3,0,0,]))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q18 Find leaders in an array (leaders: an element in an array left of which are only smaller values ex. [10, 22, 12, 3, 0, 6], here 22, 12 and 6 are leaders)

## [10, 22, 12, 3, 0, 6]

## Brute
def leaders_brute(nums):
    res = []

    for i in range(len(nums)):
        leader = True
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                leader = False
                break
        if leader:
            res.append(nums[i])
    return res

print("leaders brute: ", leaders_brute([10, 22, 12, 3, 0, 6]))

## Optimal
def leaders_optimal(nums):
    maxi = float('-inf')
    res = []
    for num in nums[::-1]:
        if num>maxi:
            maxi = num
            res.append(num)

    # return res[::-1]
    return res

print("leaders optimal: ", leaders_optimal([10, 22, 12, 3, 0, 6]))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##19 Longest Consecutive Sequence

## Brute

def longest_consecutive_brute(nums):

    longest = 0
    for num in nums:
        current = num
        count = 1

        while current+1 in nums:

            current = current+1
            count+=1

        longest = max(count, longest)

    return longest

print("longest consecutive sequence brute: ", longest_consecutive_brute([102, 4, 100, 1, 101, 3,2,1,5]))

## Better
def longest_consecutive_better(nums):

    if not nums:
        return 0

    nums.sort()

    longest = 1
    count = 0
    last_smaller = float('-inf')

    for num in nums:

        if num - 1 == last_smaller:

            count += 1
            last_smaller = num

        elif num != last_smaller:

            count = 1
            last_smaller = num

        longest = max(longest, count)

    return longest

## Optimal
def longest_consecutive_optimal(nums):

    num_set = set(nums)

    longest = 0

    for num in num_set:

        # start of sequence
        if num - 1 not in num_set:

            current = num
            count = 1

            while current + 1 in num_set:

                current += 1
                count += 1

            longest = max(longest, count)

    return longest

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q20 Set Matrix Zeroes | O(1) Space Approach | Brute - Better - Optimal
## find 0's in an NxM matrix and set that column and row to 0


## Brute

def set_matrix_brute(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    def set_row(row):
        for i in range(cols):
            if matrix[row][i] !=0:
                matrix[row][i] =-1

    def set_col(col):
        for j in range(rows):
            if matrix[j][col] != 0:
                matrix[j][col]=-1

    for r in range(rows):

        for c in range(cols):
            if matrix[r][c] == 0:
                set_row(r)
                set_col(c)

    for r in range(rows):

        for c in range(cols):
            if matrix[r][c]==-1:
                matrix[r][c]=0

    return matrix

print("set_matrix_brute: ", set_matrix_brute([
 [1,1,1],
 [1,0,1],
 [1,1,1]
]))

## optimal

def set_matrix_optimal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    col0 = 1

    for r in range(rows):
        if matrix[r][0] == 0:
            col0 = 0

        for c in range(1, cols):

            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    for r in range(1, rows):

        for c in range(1, cols):

            if matrix[0][c] == 0 or matrix[r][0] ==0:
                matrix[r][c] = 0
    if matrix[0][0] == 0:
        for i in range(cols):

            matrix[0][i] = 0

    if col0 ==0:

        for r in range(rows):
            matrix[r][0] = 0
    return matrix

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q21 Rotate a matrix by 90 degrees

## Brute

def rotate_matrix_brute(matrix):
    n = len(matrix)

    res = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            res[col][n-row-1] = matrix[row][col]
    return res

## Optimal

def rotate_matrix_optimal(matrix):
    n = len(matrix)

    for row in range(n):

        for col in range(row+1, n):

            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # STEP 2: REVERSE EACH ROW
    for row in matrix:
        row.reverse()

    return matrix


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q22 Spiral Traversal of a Matrix | Spiral Matrix

def spiral_traversal_matrix(matrix):

    res = []
    rows = len(matrix)
    cols = len(matrix[0])

    top = 0
    bottom = rows - 1

    left = 0
    right = cols - 1

    while top<=bottom and left<=right:

        ## Left to Right
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top+=1

        ## Top to Bottom

        for j in range(top, bottom+1):
            res.append(matrix[j][right])

        right -=1

        ## Right to Left

        if top<=bottom:
            for k in range(right, left-1, -1):
                res.append(matrix[bottom][k])

            bottom -=1

        ## Bottom to Top

        if left<=right:

            for l in range(bottom, top-1, -1):
                res.append(matrix[l][left])
            left+=1

    return res


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q23 Count Subarray sum Equals K | Brute - Better - Optimal

## Brute

def count_subarray_sum_brute(nums, target):
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i, n):

            sum = 0
            for k in range(i, j+1):
                sum += nums[k]
            if sum == target:
                res+=1
    return res

## Better
def count_subarray_sum_better(nums, target):

    n = len(nums)

    res = 0

    for i in range(n):

        total = 0

        for j in range(i, n):

            total += nums[j]

            if total == target:
                res += 1

    return res

## Optimal (Prefix Sum)
def count_subarray_sum_optimal(nums, k):
    mp = {0: 1}
    presum = 0
    count=0

    for i in nums:
        presum+=i

        count+=mp.get(presum-k, 0)
        mp[presum] = mp.get(presum, 0) + 1
    return count

print("count Subarray Brute:", count_subarray_sum_brute([1,2,3,-3,1,1,1,4,2,-3], 3))
print("count Subarray Better:", count_subarray_sum_better([1,2,3,-3,1,1,1,4,2,-3], 3))
print("count Subarray optimal:", count_subarray_sum_optimal([1,2,3,-3,1,1,1,4,2,-3], 3))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q24 Pascal Triangle | Finding nCr in minimal time
## Type of question: Given Row and column find the element at that place
## print Nth row of pascal triangle
## Given N print the pascal triangle

def print_pascal_triangle(row):
    triangle = []

    for r in range(row):
        temp = []

        for c in range(r+1):

            if c == 0 or c==r:
                temp.append(1)
            else:
                temp.append(triangle[r-1][c-1] + triangle[r-1][c])
        triangle.append(temp)
    return triangle


print("Pascal Triangle: ", print_pascal_triangle(6))

## Type 1: Given Row and column find the element at that place

## Brute: Make the entie triangle

## Better
import math

def pascal_better(row, col):

    n = row - 1
    r = col - 1

    return (
        math.factorial(n)
        //
        (
            math.factorial(r)
            * math.factorial(n-r)
        )
    )

## Optimal
def pascal_optimal(row, col):

    n = row - 1
    r = col - 1

    res = 1

    for i in range(r):

        res = res * (n - i)

        res = res // (i + 1)

    return res


## Type 2: print Nth row of pascal triangle

## optimal
def pascal_nth_row_optimal(n):

    ans = [1]

    res = 1

    for c in range(1, n):

        res = res * (n - c)
        res = res // c

        ans.append(res)

    return ans

## Type 3 : Given N print the pascal triangle

## Optimal

def generate_pascal_triangle(n):

    triangle = []

    for row in range(n):

        temp = [1]

        res = 1

        for col in range(1, row + 1):

            res = res * (row - col + 1)
            res = res // col

            temp.append(res)

        triangle.append(temp)

    return triangle


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q25 Majority Element II | Brute-Better-Optimal (Majority Element I use Moore's Voting Algorithm)

## Brute
def majority_element1_brute(nums):
    n = len(nums)

    res = []

    for i in nums:
        if i in res:
            continue

        count = 0
        for num in nums:
            if num == i:
                count+=1
        if count > n//3:
            res.append(i)
    return res

##  Better

def majority_element1_better(nums):

    mp = {}
    res = []
    n = len(nums)
    for i in nums:
        mp[i] = mp.get(i, 0)+1

        if mp[i] > n//3 and i not in res:
            res.append(i)
    return res

## optimal

def majority_element_optimal(nums):

    count1 = 0
    count2 = 0

    elem1 = None
    elem2 = None

    # STEP 1: FIND POTENTIAL CANDIDATES
    for num in nums:

        if elem1 == num:
            count1 += 1

        elif elem2 == num:
            count2 += 1

        elif count1 == 0:
            elem1 = num
            count1 = 1

        elif count2 == 0:
            elem2 = num
            count2 = 1

        else:
            count1 -= 1
            count2 -= 1

    # STEP 2: VERIFY CANDIDATES
    count1 = 0
    count2 = 0

    for num in nums:

        if num == elem1:
            count1 += 1

        elif num == elem2:
            count2 += 1

    res = []

    n = len(nums)

    if count1 > n // 3:
        res.append(elem1)

    if count2 > n // 3:
        res.append(elem2)

    return res

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q26 3 Sum

## Brute

def three_sum_brute(nums):
    res = set()
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):

                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    res.add(tuple(triplet))
    return [list(x) for x in res]


## Better
def three_sum_better(nums):
    n = len(nums)
    res = set()
    for i in range(n):
        seen = set()
        for j in range(i+1, n):
            third = -(nums[i]+nums[j])
            if third in seen:
                triplet = sorted([nums[i], nums[j], third])
                res.add(tuple(triplet))
            seen.add(nums[j])
    return [list(x) for x in res]

## Better
def three_sum_optimal(nums):

    nums.sort()

    n = len(nums)

    res = []

    for i in range(n):

        # SKIP DUPLICATES
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total < 0:

                left += 1

            elif total > 0:

                right -= 1

            else:

                res.append([
                    nums[i],
                    nums[left],
                    nums[right]
                ])

                left += 1
                right -= 1

                # SKIP DUPLICATES
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q27 4 sum

## Brute
def four_sum_brute(nums, target):

    n = len(nums)

    res = set()

    for i in range(n):

        for j in range(i + 1, n):

            for k in range(j + 1, n):

                for l in range(k + 1, n):

                    if nums[i] + nums[j] + nums[k] + nums[l] == target:

                        quad = sorted([
                            nums[i],
                            nums[j],
                            nums[k],
                            nums[l]
                        ])

                        res.add(tuple(quad))

    return [list(x) for x in res]

## Better
def four_sum_better(nums, target):

    n = len(nums)

    res = set()

    for i in range(n):

        for j in range(i + 1, n):

            seen = set()

            for k in range(j + 1, n):

                fourth = target - (
                    nums[i] +
                    nums[j] +
                    nums[k]
                )

                if fourth in seen:

                    quad = sorted([
                        nums[i],
                        nums[j],
                        nums[k],
                        fourth
                    ])

                    res.add(tuple(quad))

                seen.add(nums[k])

    return [list(x) for x in res]

## Optimal
def four_sum_optimal(nums, target):

    nums.sort()

    n = len(nums)

    res = []

    for i in range(n):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):

            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:

                total = (
                    nums[i]
                    + nums[j]
                    + nums[left]
                    + nums[right]
                )

                if total < target:

                    left += 1

                elif total > target:

                    right -= 1

                else:

                    res.append([
                        nums[i],
                        nums[j],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    while (
                        left < right
                        and nums[left] == nums[left - 1]
                    ):
                        left += 1

                    while (
                        left < right
                        and nums[right] == nums[right + 1]
                    ):
                        right -= 1

    return res


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q28 Number of Subarrays with xor K | Brute - Better - Optimal

## Brute
def subarray_xor_brute(nums, target):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i, n):
            xor = 0
            for k in range(i, j+1):
                xor ^= nums[k]
            if xor == target:
                count+=1
    return count

## Better
def subarray_xor_better(nums, target):
    n = len(nums)
    count = 0

    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor ^= nums[j]
            if xor == target:
                count+=1
    return count


## Optimal
def subarray_xor_optimal(nums, k):
    xor = 0
    count = 0
    mp = {0:1}

    for num in nums:
      xor ^=num
      count += mp.get(xor^k, 0)
      mp[xor] = mp.get(xor, 0)+1
    return count

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q29 Merge Overlapping Intervals | Brute, Optimal with Precise TC analysis

## Brute
def merge_overlapping_brute(nums):
    res = []
    nums.sort()
    n = len(nums)

    for i in range(n):
        start = nums[i][0]
        end = nums[i][1]

        if res and end<=res[-1][1]:
            continue

        for j in range(i+1, n):
            if nums[j][0] <=end:
                end = max(nums[j][1], end)

            else:
                break

        res.append([start, end])
    return res

print("merge overlap intervals Brute: ", merge_overlapping_brute([[1,3],[2,6],[8,10],[15,18]]))

## Optimal
def merge_overlapping_optimal(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        if not res or nums[i][0]>res[-1][1]:
            res.append(nums[i])
        else:
            res[-1][1] = max(res[-1][1], nums[i][1])

    return res

print("merge overlap intervals opt: ", merge_overlapping_optimal([[1,3],[2,6],[8,10],[15,18]]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q29 Merge Sorted Arrays Without Extra Space | 2 Optimal Solution

## Brute (using extra space)
def merge_sorted_brute(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    res = []
    i, j = 0, 0

    while i<n and j <m:
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i+=1
        else:
            res.append(nums2[j])
            j+=1
    while i < n:
        res.append(nums1[i])
        i+=1
    while j < m:
        res.append(nums2[j])
        j+=1
    for i in range(len(res)):
        if i < n:
            nums1[i] = res[i]
        else:
            nums2[i-n] = res[i]
    return nums1, nums2

print("merge_sorted brute:", merge_sorted_brute([1,3,5,7,9], [0,2,4,6,8]))

## Optimal 1
def merge_sorted_opt1(nums1, nums2):
    left = len(nums1)-1
    right = 0
    while left>=0 and right< len(nums2):
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]
            left-=1
            right+=1
        else:
            break
    nums1.sort()
    nums2.sort()
    return nums1, nums2
print("merge_sorted opt1 :", merge_sorted_opt1([1,3,5,7,9], [0,2,4,6,8]))

## Optimal 2
def next_gap(gap):

    if gap <= 1:
        return 0

    return (gap // 2) + (gap % 2)
def merge_sorted_opt2(nums1, nums2):

    n = len(nums1)
    m = len(nums2)

    gap = next_gap(n + m)

    while gap > 0:

        left = 0
        right = left + gap

        while right < n + m:

            # both pointers in nums1
            if left < n and right < n:

                if nums1[left] > nums1[right]:
                    nums1[left], nums1[right] = \
                    nums1[right], nums1[left]

            # left in nums1, right in nums2
            elif left < n and right >= n:

                if nums1[left] > nums2[right - n]:
                    nums1[left], nums2[right - n] = \
                    nums2[right - n], nums1[left]

            # both pointers in nums2
            else:

                if nums2[left - n] > nums2[right - n]:
                    nums2[left - n], nums2[right - n] = \
                    nums2[right - n], nums2[left - n]

            left += 1
            right += 1

        gap = next_gap(gap)

    return nums1, nums2

print("merge_sorted opt2 :", merge_sorted_opt2([1,3,5,7,9], [0,2,4,6,8]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q30 Find the Missing and Repeating Number | 4 Approaches

## Brute
def missing_and_repeating_brute(nums):
    n = len(nums)
    repeating, missing = -1,-1
    for i in range(1,n+1):
        count = 0
        for j in nums:
            if j == i:
                count+=1
        if count==2:
            repeating = i
        elif count == 0:
            missing = i
    return repeating, missing

print('missing/repeating brute:', missing_and_repeating_brute([4,6,3,2,1,1]))


## Better
def missing_and_repeating_better(nums):
    n = len(nums)
    hashmap = [0]*(n+1)
    repeating, missing = -1,-1
    for i in nums:
        hashmap[i]+=1

    for j in range(1,len(hashmap)):
        if hashmap[j] == 2:
            repeating = j
        elif hashmap[j] ==0:
            missing = j
    return repeating, missing
print('missing/repeating better:', missing_and_repeating_better([4,6,3,2,1,1]))

## Optimal (sum of n natural numbers)
def missing_and_repeating_opt(nums):
    n = len(nums)
    SN = (n*(n+1))/2
    SN2 = (n*(n+1)*(2*n+1))/6
    S, S2 = 0, 0
    # x - y = S - SN
    # x2 - y2 = S2 - SN2

    for i in range(n):
        S += nums[i]
        S2 += nums[i]*nums[i]
    val1 = S - SN
    val2 = (S2 - SN2)/val1
    x = (val1 + val2)/2
    y = x-val1
    return int(x), int(y)
print('missing/repeating opt:', missing_and_repeating_opt([4,6,3,2,1,1]))

## Optimal (XOR/Bit Manipulation)
def missing_and_repeating_xor(nums):

    n = len(nums)

    xor = 0

    # XOR array
    for num in nums:
        xor ^= num

    # XOR 1..n
    for i in range(1, n + 1):
        xor ^= i

    # rightmost set bit
    bit = xor & -xor

    bucket1 = 0
    bucket2 = 0

    # partition array
    for num in nums:

        if num & bit:
            bucket1 ^= num
        else:
            bucket2 ^= num

    # partition 1..n
    for i in range(1, n + 1):

        if i & bit:
            bucket1 ^= i
        else:
            bucket2 ^= i

    # determine which is repeating
    count = 0

    for num in nums:
        if num == bucket1:
            count += 1

    if count == 2:
        repeating = bucket1
        missing = bucket2
    else:
        repeating = bucket2
        missing = bucket1

    return repeating, missing
print('missing/repeating xor:', missing_and_repeating_xor([4,6,3,2,1,1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q31 Count Inversions in an Array | Brute and Optimal

## Brute
def count_inversion_brute(nums):
    count = 0
    n = len(nums)

    for i in range(0, n-1):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                count+=1
    return count
