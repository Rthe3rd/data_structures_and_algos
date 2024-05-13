# Recursion

# A function that call itself, until it doesn't

# Base case: The condition when the function will stop calling itself
    # Statement that is trigger -> think ball in boxes.
    # Must be a return statement so that the program does not continue
# Recusive case: The condition when the function will call itself
# Problem should be getting smaller with each recursive call 


# Callstack
# Can be thought of like the stack data structure; the top function is the one to run next and once it is done running, then the next function can be ran and so on

# Factorial 
# Classic recursive example  
# 4! => n = 4 or factorial(4)
    # = 4 * 3! => return n * factorial(n - 1 = 3)
    # = 4 * 3 * 2! => return n * factorial(n - 1 = 2)
    # = 4 * 3 * 2 * 1! => return n * factorial(2-1)
    # = 4 * 3 * 2 * 1 * 1 => base case whe n == 1
        # Once you reach your base case, you "bubble up" what was returned from the base case
        # return 1 => base case
        # return 2 * 1 => where 1 is the return from the n - 1 = 1 case or "base case"
        # return 3 * 2 => where 2 is the return from the n - 1 = 2 case
        # return 4 * 6 => where 6 is the return from the n - 1 = 3 case

# You can also think of it as a call stack, nothing is returned until the base case is met or "stacked" on the stack last and then ran

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))

