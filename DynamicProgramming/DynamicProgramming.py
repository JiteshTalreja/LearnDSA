"""
What DP really is (no textbook definition)

DP = avoid recomputing overlapping subproblems

or even better:

Recursion + Caching (memoization) OR Tabulation
🔥 The Only Mental Model You Need

Every DP problem can be broken into:

1. State
2. Transition
3. Base case
"""

## TOP DOWN

memo = [None]*100
count = 0

def fibo(n):
    global count
    count+=1
    if memo[n] is not None:
        return memo[n]

    if n <=1:
        return n

    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(99))
print(count)


"""
🧠 First: What does “Bottom-Up” mean?

Start from the smallest problems → build up to the final answer

Contrast with Top-Down
Approach	Idea
Top-down	recursion + memo
Bottom-up	build from base cases
🔢 Fibonacci Reminder
f(n) = f(n-1) + f(n-2)

Base:

f(0) = 0
f(1) = 1
🧠 Bottom-Up Thinking

Instead of asking:

What is f(5)?

You say:

Let me compute:
f(0), f(1), f(2), f(3), ..., f(5)
📊 Build Step-by-Step
i    value
---------
0 → 0
1 → 1
2 → 1
3 → 2
4 → 3
5 → 5
"""


def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]