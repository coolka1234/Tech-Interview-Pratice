# Given a positive integer N, find the Nth Even Fibonacci number. Since the answer can be very large, return the answer modulo 1000000007.

# Example 1:

# Input: n = 1
# Output: 2 
# Explanation: 2 is the first even
# number in the fibonacci series.

# Example 2:

# Input: n = 2
# Output: 8
# Explanation: 8 is the second even
# number in the fibonacci series.


# Your Task:  
# You dont need to read input or print anything. Complete the function nthEvenFibonacci() which takes S as input parameter and returns the Nth even fibonacci number.
def even_fibonacci(n):
    counter=0
    f1=1
    f2=1
    while counter<n:
        old_f2=f2
        f2=f1+f2
        f1=old_f2
        if f2%2==0:
            counter+=1
    return f2%1000000007



if __name__=='__main__':
    n=12
    print(even_fibonacci(n))