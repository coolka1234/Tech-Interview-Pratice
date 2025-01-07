# Given a number N. Find the last two digits of the Nth fibonacci number.
# Note: If the last two digits are 02, return 2.

# Example 1:

# Input:
# N = 13
# Output:
# 33
# Explanation:
# The 13th Fibonacci number is 233.
# So last two digits are 3 and 3.

# Example 2:

# Input:
# N = 255
# Output:
# 70
# Explanation:
# The 255th fibonacci number is  875715953430-
# 18854458033386304178158174356588264390370.
# Thus, last two digits are 7 and 0.


# Your Task:
# You don't need to read input or print anything.Your task is to complete the function fibonacciDigits() which takes a number N as input parameter and returns the last two digits of the Nth fibonacci number.


# Expected Time Complexity:O(K)
# Expected Auxillary Space:O(K)
# K is of the order 102.

def calc_fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return calc_fib(n-1)+calc_fib(n-2)    

print(calc_fib(33))

def last_two_dig(n):
    last=0
    sec_last=0
    return n % 100 

print(last_two_dig(calc_fib(33)))