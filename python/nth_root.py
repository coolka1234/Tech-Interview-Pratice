# You are given 2 numbers (n , m); the task is to find n√m (nth root of m).
 

# Example 1:

# Input: n = 2, m = 9
# Output: 3
# Explanation: 32 = 9

# Example 2:

# Input: n = 3, m = 9
# Output: -1
# Explanation: 3rd root of 9 is not
# integer.

 

# Your Task:
# You don't need to read or print anyhting. Your task is to complete the function NthRoot() which takes n and m as input parameter and returns the nth root of m. If the root is not integer then returns -1.
 

# Expected Time Complexity: O(n* log(m))
# Expected Space Complexity: O(1)
 

# Constraints:
# 1 <= n <= 30
# 1 <= m <= 109         
def find_root(n, m):
    for number in m:
        if pow(n, number)==m:
            return number
    return -1

if __name__=='__main__':
    n, m=2, 9
    print(find_root())