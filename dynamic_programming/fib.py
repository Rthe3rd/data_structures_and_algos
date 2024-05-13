# Dynamic Programming
# Used when you have overlapping sub-problems with optimal sub structures

# Top Down vs. Bottom Up

# Top Down
# First thing we try to solve is the highest number.  It is the first thing that goes on the call stack. Fib(n) works from n => 0
# Bottom Down
# First thing we try to solve is the lowest number.  Iteratively

# Memoization
# Saving results of subproblems in a cache, list in this instance, in order to get solutions without having to re-run the sub-problem (function)
# If you are doing recursion + dynamic programming, you need to be using memoization in order to prevent the number of function calls from exploding

# Fibonaci sequence
# Big O: Without memoization: O(2^n) vs. with memoization: O(2n - 1) => O(n)
# Top down method: recursion
memo = [None] * 100
counter = 0
def fib(n):
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n

    # Saving value into the cache
    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


n = 35
print(f"\nFib of {n} = {fib(n)}")
print(f'Counter: {counter}')

counter_bottom_up = 0
# Bottom up fibonaci sequence
# Big O: O(n-1) => O(n)
def fib_bottom_up(n):
    fib_list = [0,1]
    # Iteratively loop from 2 to n (note the n + 1 boundary on range())
    for index in range(2, n + 1):
        global counter_bottom_up
        counter_bottom_up += 1
        next_fib = fib_list[index-1] + fib_list[index-2]
        fib_list.append(next_fib)
    return fib_list[n]


print(f"\nFib_bottom_up of {n} = {fib_bottom_up(n)}")
print(f'Counter: {counter_bottom_up}')

