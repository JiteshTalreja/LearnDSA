"""
Set: Find Pairs ( ** Interview Question)
You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.

Assume that each array does not contain duplicate values.

The tests for this exercise assume that arr1 is the list being converted to a set.

Pairs should be returned in the order they are found while iterating through arr2.

Input

Your function should take in the following inputs:

arr1: a list of integers

arr2: a list of integers

target: an integer



Output

Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.
The first element of each tuple should be from arr1 and the second from arr2.
Example 1:

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
target = 9

pairs = find_pairs(arr1, arr2, target)
print(pairs)
# Expected output: [(3, 6)]
# Explanation: There's only one pair that adds up to 9: 3 from arr1 and 6 from arr2.


Example 2:

arr1 = [0, 1, 2]
arr2 = [7, 8, 9]
target = 10

pairs = find_pairs(arr1, arr2, target)
print(pairs)
# Expected output: [(3, 7), (2, 8), (1, 9)]
# Explanation: The pairs that add up to 10 are (3, 7), (2, 8), and (1, 9).
# They appear in arr2 iteration order.


Example 3:

arr1 = [1, 2, 3, 5]
arr2 = [1, 3, 4, 5]
target = 6

pairs = find_pairs(arr1, arr2, target)
print(pairs)
# Expected output: [(5, 1), (3, 3), (2, 4), (1, 5)]
# Explanation: The pairs that add up to 6 are (5, 1), (3, 3),
# (2, 4), and (1, 5). Each pair consists of one element from arr1
# and one element from arr2 that together sum to the target value.


Example 4:

arr1 = [1, 2, 3, 5]
arr2 = [1, 3, 4, 5]
target = 11

pairs = find_pairs(arr1, arr2, target)
print(pairs)
# Expected output: []
# Explanation: There are no pairs in arr1 and arr2 that add up to 11.

"""


def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []

    for i in arr2:
        if target - i in set1:
            pairs.append((target - i, i))
    return pairs


""""Set: Longest Consecutive Sequence ( ** Interview Question)
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.

Example:



Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.


"""

def longest_consecutive_sequence(arr):

    set1 = set(arr)
    longest = 0

    for i in arr:
        if i-1 not in set1:
            current = i
            cur_seq = 1

            while current +1 in set1:
                current +=1
                cur_seq +=1

            longest= max(longest, cur_seq)
    return longest

print(longest_consecutive_sequence([100, 3, 4,5, 2, 1, 200, 101, 102]))