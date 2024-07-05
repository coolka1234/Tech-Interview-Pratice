# Given a number n.Find if the digit sum(or sum of digits) of n is a Palindrome number or not.

# Note: A Palindrome number is a number that stays the same when reversed. Example- 121 , 131 , 7 etc.

# Example 1:

# Input:
# n = 56
# Output: 1
# Explanation:
# The digit sum of 56 is 5+6=11.Since, 11 is a palindrome number.Thus, answer is 1.

# Example 2:

# Input:
# n = 98
# Output: 0
# Explanation:
# The digit sum of 98 is 9+8=17. Since 17 is not a palindrome,thus, answer is 0.

# Your Task:
# You don't need to read input or print anything.Your Task is to complete the function isDigitSumPalindrome() which takes a number n as input parameter and returns 1 if the Digit sum of n is a palindrome. Otherwise, it returns 0.

# Expected Time Complexity: O(log(n))
# Expected Auxillary Space: O(1)

# Constraints:
# 1 <= n <= 109
from xml.etree.ElementTree import tostring


def sum_digist(num):
    sum=0
    while num > 0:
        digit=num%10
        num=int(num/10)
        sum+=digit
    return sum

def palindrome_digi_check(num)->bool:
    num_sum=sum_digist(num)
    array_num_sum=str(num_sum)
    for i in range(0,int(len(array_num_sum)/2)-1):
        if array_num_sum[i]!=array_num_sum[len(array_num_sum)-i]:
            return False
    return True

if __name__=='__main__':
    print(sum_digist(153))
    print(palindrome_digi_check(1531))
