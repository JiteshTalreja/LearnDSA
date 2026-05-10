"""
Q1 Print name 5 time
"""

def print_name(name, n, count):
    if count >= n:
        return
    print(name)
    print_name(name, n, count+1)

"""
Q2 print from 1 to N
"""

def print_1_to_n(n):
    if n <=0:
        return
    print_1_to_n(n-1)
    print(n)


"""
Q3 print N to 1
"""

def print_n_to_1(n):

    if n <= 0:
        return
    print(n)
    print_n_to_1(n-1)

"""
Q4 sum of first N number 
"""

## parameterized way (simply said, calling same function with different parameters)

def sum_n(n, sum):
    if n < 1:
        print(sum)
        return 0
    sum_n(n-1, sum+n)

sum_n(10, 0)

## Functional

def sum_n_func(n):
    if n <=0:
        return 0
    return n + sum_n_func(n-1)

sum_n_func(10)


"""
Q5 Reverse a list using recursion
"""
def reverse_list(nums, i, n):
    if i>=n:
        return
    nums[i], nums[n] = nums[n], nums[i]
    reverse_list(nums, i+1, n-1)
    return nums

"""
Q6 check palindrome
"""


def is_palindrome(string, i):
    n = len(string)

    if i >= n // 2:
        return True

    if string[i] != string[n - i - 1]:
        return False
    return is_palindrome(string, i + 1)


"""
Q7 Fibonacci series 
    (recursion tree )
    
        n
      /   \
    n-1   n-2
   /   \
 n-2   n-3
"""

def nth_fibonacci(n):

    if n<=1:
        return n

    return nth_fibonacci(n-1) + nth_fibonacci(n-2)


"""
Q8 print all subsequences

def func(index, arr):
    if index == len(arr):
        # base condition
        return

    # pick
    func(index + 1)

    # not pick
    func(index + 1)
"""


def print_subsequences(nums):

    result = []

    def backtrack(index, path):

        # base case
        if index == len(nums):
            result.append(path[:])
            return

        # TAKE
        path.append(nums[index])
        backtrack(index + 1, path)

        # BACKTRACK
        path.pop()

        # NOT TAKE
        backtrack(index + 1, path)

    backtrack(0, [])

    return result

print(print_subsequences([3,1,2]))

"""
Q9 Print all subsequences that make sum k 
"""
def print_subsequences_sum_k(nums, k):
    result = []
    def backtrack(index, path, current_sum):

        # base case
        if index == len(nums):

            if current_sum == k:
                result.append(path[:])

            return

        # TAKE
        path.append(nums[index])

        backtrack(
            index + 1,
            path,
            current_sum + nums[index]
        )

        # BACKTRACK
        path.pop()

        # DON'T TAKE
        backtrack(
            index + 1,
            path,
            current_sum
        )

    backtrack(0, [], 0)
    return result


print("subsequence with sum k :", print_subsequences_sum_k([1,2,1], 2))

"""
Q10 Print only one subsequences that make sum k 
"""
def print_one(index, arr, ds, s, k):
    if index == len(arr):
        if s == k:
            print(ds)
            return True
        return False

    # pick
    ds.append(arr[index])

    if print_one(index + 1, arr, ds, s + arr[index], k):
        return True

    ds.pop()

    # not pick
    if print_one(index + 1, arr, ds, s, k):
        return True

    return False


"""
Q11 Count Subsequences with Sum = K
"""

def count_subseq(index, arr, s, k):
    if index == len(arr):
        if s == k:
            return 1
        return 0

    # pick
    left = count_subseq(index + 1, arr, s + arr[index], k)

    # not pick
    right = count_subseq(index + 1, arr, s, k)

    return left + right

"""
Combination Sum:
"""
"""
| Problem            | Reuse allowed? | Duplicates in input? |
| ------------------ | -------------- | -------------------- |
| Combination Sum I  | ✅ Yes          | ❌ Distinct           |
| Combination Sum II | ❌ No           | ✅ Yes                |

🧠 Core Idea

Combination Sum is a classic recursion + backtracking problem where we try to build all possible combinations whose sum equals a target.

At every step we make a decision:

1. Pick current element
2. Do not pick current element

This creates a decision tree (DFS traversal).

🔥 Key Concepts
1. Recursion

We recursively explore all possible combinations.

Each recursive call represents:

current state of combination
2. Backtracking

Backtracking means:

make choice → recurse → undo choice

Pattern:

append
recurse
pop

The pop() step restores previous state so other branches can be explored.

🌳 Decision Tree Thinking

For every element:

take / not take

This forms a recursion tree of possibilities.

Example:

[]
├── take 2
│   ├── take 2
│   └── skip 2
└── skip 2
🟢 Combination Sum I
Rules
Input elements are distinct
Same element can be reused multiple times
Important recursion behavior

When taking an element:

backtrack(index, ...)

We stay on same index because reuse is allowed.

🔴 Combination Sum II
Rules
Input may contain duplicates
Each element can be used only once
Output combinations must be unique
Important recursion behavior

When taking an element:

backtrack(index + 1, ...)

Move forward because reuse is NOT allowed.
"""


"""
Q12 Combination Sum I
"""

def combination_sum(nums, target):
    res = []

    def backtracking(index, path, total):

        # found answer
        if total == target:
            res.append(path[:])
            return

        if total > target or index >= len(nums):
            return

        # PICK current element
        path.append(nums[index])
        backtracking(index, path, total + nums[index])

        # BACKTRACK
        path.pop()

        # NOT PICK
        backtracking(index + 1, path, total)

    backtracking(0, [], 0)
    return res

print("combination sum I: ", combination_sum([2,2,3], 7))


"""
Q13 Combination Sum II

| Problem            | Reuse allowed? | Duplicates in input? |
| ------------------ | -------------- | -------------------- |
| Combination Sum I  | ✅ Yes          | ❌ Distinct           |
| Combination Sum II | ❌ No           | ✅ Yes                |

"""

def combination_sum2(nums, target):
    nums.sort()
    res = []

    def backtrack(start, path, total):

        # found answer
        if total == target:
            res.append(path[:])
            return

        # exceeded target
        if total > target:
            return

        for i in range(start, len(nums)):

            # SKIP DUPLICATES
            if i > start and nums[i] == nums[i - 1]:
                continue

            # pruning
            if total + nums[i] > target:
                break

            path.append(nums[i])

            # move to next index (NO reuse)
            backtrack(i + 1, path, total + nums[i])

            path.pop()

    backtrack(0, [], 0)
    return res

print("combination sum I: ", combination_sum2([1,1,1,2,2], 4))