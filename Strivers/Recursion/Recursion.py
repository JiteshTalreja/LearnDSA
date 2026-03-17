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