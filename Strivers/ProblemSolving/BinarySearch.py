"""
================================================================================
BINARY SEARCH - Theory & Mental Models
================================================================================

CORE IDEA
---------
Binary Search is a divide-and-conquer search strategy that works on a
*sorted (or monotonic)* search space. At each step, you eliminate half
the remaining candidates by comparing against the midpoint.

Time  : O(log n)
Space : O(1) iterative | O(log n) recursive (call stack)

WHY log n?
  - At each step, search space halves: n → n/2 → n/4 → ... → 1
  - Number of steps = how many times can you halve n before hitting 1?
  - That's log₂(n). For n = 1,000,000 → only ~20 comparisons.

--------------------------------------------------------------------------------
THE INVARIANT (Most Important Mental Model)
--------------------------------------------------------------------------------
Binary Search works because of a maintained invariant:

    "The answer always lies within [lo, hi] at every iteration."

Your job is to write conditions that SHRINK [lo, hi] while PRESERVING
this invariant — never accidentally discarding the answer.

--------------------------------------------------------------------------------
THE THREE TEMPLATES
--------------------------------------------------------------------------------

TEMPLATE 1 — Exact Match (find target or return -1)
  lo, hi = 0, n - 1
  while lo <= hi:
      mid = lo + (hi - lo) // 2     ← avoids integer overflow (habit from C++)
      if arr[mid] == target:
          return mid
      elif arr[mid] < target:
          lo = mid + 1
      else:
          hi = mid - 1
  return -1

  Loop condition : lo <= hi (inclusive both ends)
  Termination    : lo > hi (search space exhausted)
  Used when      : you need an exact value or index

----------

TEMPLATE 2 — Left Boundary (first occurrence / lower_bound)
  lo, hi = 0, n
  while lo < hi:
      mid = lo + (hi - lo) // 2
      if arr[mid] < target:
          lo = mid + 1
      else:
          hi = mid             ← hi narrows, never lo+1 when condition met
  return lo  # lo == hi, first index where arr[i] >= target

  Loop condition : lo < hi (hi is exclusive)
  Termination    : lo == hi (converged to single answer)
  Used when      : first position satisfying a condition

----------

TEMPLATE 3 — Right Boundary (last occurrence / upper_bound)
  lo, hi = 0, n
  while lo < hi:
      mid = lo + (hi - lo + 1) // 2    ← ceiling mid to avoid infinite loop
      if arr[mid] > target:
          hi = mid - 1
      else:
          lo = mid
  return lo

  ⚠️ Key trap: when lo = mid is possible, mid must be ceiling
     (lo + hi + 1) // 2 to prevent infinite loop where lo never moves.

  Used when : last position satisfying a condition

--------------------------------------------------------------------------------
THE MONOTONIC PREDICATE PATTERN (Most Powerful Generalization)
--------------------------------------------------------------------------------
Binary Search isn't just for sorted arrays. It applies to ANY search space
where a predicate is monotonic — i.e., FFFFFTTTTT or TTTTTFFFFF.

  Pattern:
    "Find the FIRST index where predicate(x) = True"
    or
    "Find the LAST index where predicate(x) = False"

  lo, hi = lower_bound, upper_bound
  while lo < hi:
      mid = lo + (hi - lo) // 2
      if predicate(mid):
          hi = mid      # mid could be answer, don't discard
      else:
          lo = mid + 1  # mid definitely not the answer
  return lo

  This is the engine behind "Binary Search on Answer" problems:
    - Minimum speed to finish within D days
    - Minimum capacity to ship packages in K days
    - Kth smallest in a matrix
    - Minimum days to make M bouquets
    All reduce to: "is X feasible?" → binary search on X.

--------------------------------------------------------------------------------
MID CALCULATION — Why lo + (hi - lo) // 2
--------------------------------------------------------------------------------
  Naive   : mid = (lo + hi) // 2   → can overflow in C++/Java for large ints
  Safe    : mid = lo + (hi - lo) // 2
  Python  : integers don't overflow, so (lo + hi) // 2 is fine,
            but the safe form is good habit for interviews.

  Floor mid (default) : (lo + hi) // 2     → used with hi = mid
  Ceiling mid         : (lo + hi + 1) // 2 → used with lo = mid (avoids loop)

  Rule of thumb:
    if you write  lo = mid  → use ceiling mid
    if you write  hi = mid  → use floor mid

--------------------------------------------------------------------------------
BINARY SEARCH ON ANSWER — Framework
--------------------------------------------------------------------------------
  Problem shape: "Find minimum/maximum X such that condition(X) is satisfiable"

  Steps:
  1. Define the search space [lo, hi] (lo = min possible, hi = max possible)
  2. Write a feasibility function: can_achieve(mid) → bool
  3. Apply Template 2 (find leftmost True) or Template 3 (find rightmost False)

  Example mental check:
    - "Minimum X" → FFFFF...TTTT → find first True  → Template 2
    - "Maximum X" → TTTT...FFFF  → find last True   → Template 3

--------------------------------------------------------------------------------
ROTATED SORTED ARRAYS
--------------------------------------------------------------------------------
Binary Search still works — you just need to identify which half is sorted:

  if arr[lo] <= arr[mid]:        # left half is sorted
      if arr[lo] <= target < arr[mid]:
          hi = mid - 1
      else:
          lo = mid + 1
  else:                          # right half is sorted
      if arr[mid] < target <= arr[hi]:
          lo = mid + 1
      else:
          hi = mid - 1

--------------------------------------------------------------------------------
COMMON PITFALLS
--------------------------------------------------------------------------------
1. Off-by-one errors     → always trace through lo=0, hi=1 (2-element array)
2. Infinite loop         → when lo = mid is used without ceiling mid
3. Wrong boundary        → forgetting whether hi is inclusive or exclusive;
                           be consistent within one template
4. Skipping the answer   → using mid+1 or mid-1 when mid itself could be valid
5. Wrong feasibility fn  → the binary search is only as good as can_achieve()

--------------------------------------------------------------------------------
COMPLEXITY CHEAT SHEET
--------------------------------------------------------------------------------
  Standard BS on array          : O(log n) time, O(1) space
  BS on answer (with O(n) check): O(n log(search_space)) time
  BS on 2D matrix (n×m)         : O(log(n*m)) = O(log n + log m)

--------------------------------------------------------------------------------
WHEN TO REACH FOR BINARY SEARCH
--------------------------------------------------------------------------------
Signal phrases in a problem:
  - "sorted array / matrix"
  - "find first / last / minimum / maximum satisfying X"
  - "minimize the maximum" or "maximize the minimum"
  - "K-th smallest/largest"
  - "feasible within D days / K operations"
  - Search space is large but checking a candidate is cheap

--------------------------------------------------------------------------------
PYTHON BUILT-INS (bisect module)
--------------------------------------------------------------------------------
  import bisect

  bisect.bisect_left(arr, x)   # first index where arr[i] >= x  (Template 2)
  bisect.bisect_right(arr, x)  # first index where arr[i] >  x  (upper_bound)
  bisect.insort_left(arr, x)   # insert x maintaining sorted order

  Use in interviews to verify or as utility; implement manually to demonstrate
  understanding.

================================================================================

--------------------------------------------------------------------------------
WHEN TO THINK OF BINARY SEARCH?
--------------------------------------------------------------------------------
Train your brain to pattern-match these signals immediately:

STRUCTURAL SIGNALS (the input tells you)
  * Sorted Array                  → classic BS, or boundary search
  * Sorted / Row-col sorted Matrix→ BS on flattened index or eliminate row/col
  * Rotated Sorted Array          → modified BS with half-sorted invariant
  * Infinite / Very Large Range   → BS on answer space, not array index

PROBLEM TYPE SIGNALS (the ask tells you)
  * Search / Find target          → exact match Template 1
  * First / Last Occurrence       → left/right boundary Template 2 / 3
  * Lower Bound / Upper Bound     → bisect_left / bisect_right equivalent
  * Count of elements in range    → upper_bound(x) - lower_bound(x)

OPTIMIZATION SIGNALS (hardest to recognize — most valuable in interviews)
  * "Minimum possible maximum"    → BS on answer, feasibility check
  * "Maximum possible minimum"    → BS on answer, feasibility check
  * "Smallest X such that ..."    → find first True in FFFTTT space
  * "Largest X such that ..."     → find last True in TTTFFF space
  * "Can we achieve X in K steps" → binary search on X, simulate for check
  * "At least / At most K"        → threshold-style BS on answer

KEYWORD TRIGGERS (from actual LeetCode / interview problem statements)
  ┌─────────────────────────────────────┬──────────────────────────────────┐
  │ Keyword / Phrase                    │ BS Pattern                       │
  ├─────────────────────────────────────┼──────────────────────────────────┤
  │ "sorted", "ascending", "monotonic"  │ Classic array BS                 │
  │ "find position", "search"           │ Exact match or boundary          │
  │ "first/last true", "pivot"          │ Left/right boundary              │
  │ "minimum days/speed/capacity"       │ BS on answer (minimize)          │
  │ "maximum K", "at most"              │ BS on answer (maximize)          │
  │ "K-th smallest/largest"             │ BS on value space + count check  │
  │ "allocate", "divide into K parts"   │ BS on answer (partition check)   │
  │ "within D days", "in K operations"  │ BS on answer (feasibility)       │
  └─────────────────────────────────────┴──────────────────────────────────┘

THE SMELL TEST — ask yourself these 3 questions:
  1. Is the search space ordered / monotonic in some way?
  2. Can I write a yes/no feasibility check for a candidate value?
  3. Does the answer have a clear lower and upper bound I can define?

  If YES to all 3 → Binary Search on Answer, almost certainly.
  If YES to 1 only → Classic array/index Binary Search.

--------------------------------------------------------------------------------

"""
from annotationlib import annotations_to_string


## Binary search using Recursion

def bs_recursive(nums, target, left = 0, right = None):

    if right is None:
        right = len(nums)-1

    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return nums[mid]
    elif nums[mid] > target:
        return bs_recursive(nums, target, left, mid-1)
    else:
        return bs_recursive(nums, target, mid+1, right)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q1 Implement Lower Bound and Upper Bound | Search Insert Position | Floor and Ceil
# Lower Bound: lowest index i such that nums[i]>= target

## [1,2,3,3,5,8,8,10,10,11]
#recursion
def lower_bound_rec(nums, target):

    def helper(left, right, ans):
        if left > right:
            return ans

        mid = left + (right-left)//2

        if nums[mid]>=target:
            ans = mid
            return helper(left, mid-1, ans)
        else:
            return helper(mid+1, right,ans)

    return helper(0, len(nums)-1, len(nums))
print('lower bound rec: ', lower_bound_rec([1,2,3,3,5,8,8,10,10,11], 4))

#for loop

def lower_bound_loop(nums, target):
    ans = len(nums)
    left = 0; right = len(nums)-1

    while left <= right:
        mid = left + (right - left)//2

        if nums[mid]>=target:
            ans = mid
            right = mid - 1
        else:
            left = mid+1
    return ans
print('lower bound loop: ', lower_bound_loop([1,2,3,3,5,8,8,10,10,11], 4))

# Upper Bound: lowest index i such that nums[i]> target

def upper_bound_rec(nums, target):
    def helper(left, right, ans):
        if left > right:
            return ans

        mid = left + (right-left)//2

        if nums[mid]>target:
            ans = mid
            return helper(left, mid-1, ans)
        else:
            return helper(mid+1, right, ans)

    return helper(0,len(nums)-1, len(nums))
print('Upper bound rec: ', upper_bound_rec([1,2,3,3,4,5,8,8,10,10,11], 4))

def upper_bound_loop(nums, target):
    ans = len(nums)
    left = 0; right =len(nums)-1

    while left <= right:
        mid = left + (right - left)//2

        if nums[mid] > target:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    return ans
print('Upper bound rec: ', upper_bound_loop([1,2,3,3,4,5,8,8,10,10,11], 4))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q2 Search Insert Position | given an array nums and a target value you are to find the exact index of the target value in nums, if target not in nums find
# index where it should be present

## same as lowe bound

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q3 Floor and Ceil
## floor = largest number in array <= target ----> can be done using lower-bound
## ceil = smallest number in array >= target ----> lower bound


def floor_value(nums, target):
    ans = -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            ans = nums[mid]      # possible floor
            left = mid + 1       # try finding a larger valid value
        else:
            right = mid - 1

    return ans

def floor_value_rec(nums, target):
    def helper(left, right, ans):
        if left > right:
            return ans
        mid = left +(right-left)//2

        if nums[mid]<=target:
            return helper(mid+1, right, mid)
        else:
            return helper(left, mid-1, ans)
    return helper(0, len(nums)-1, -1)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
##Q4 BS-3. First and Last Occurrences in Array | Count occurrences in Array

## Brute
def first_last(nums, target):
    first = -1 ; last = -1

    for i, v in enumerate(nums):
        if v == target:
            if first ==-1:
                first = i
            last = i
    return first, last

print('first and last occurrence: ', first_last([2,4,6,8,8,8,11,13], 8))

## using lower bound upper bound

def first_last_ublb(nums, target):
    def lower_bound(left, right, ans):
        if left > right:
            return ans

        mid = left + (right-left)//2

        if nums[mid]>=target:
            ans = mid
            return lower_bound(left, mid-1, ans)
        else:
            return lower_bound(mid+1, right, ans)

    def upper_bound(left, right, ans):
        if left>right:
            return ans
        mid = left + (right-left)//2

        if nums[mid]>target:
            ans = mid
            return upper_bound(left, mid-1, ans)
        else:
            return upper_bound(mid+1, right, ans)

    first = lower_bound(0, len(nums)-1, len(nums))
    last = upper_bound(0, len(nums)-1, len(nums))-1
    return first, last

print('first and last occurrence: ', first_last_ublb([2,4,6,8,8,8,11,13], 8))