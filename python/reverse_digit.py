# You are given an integer N, reverse the digits of given number N, ensuring that the reversed number has no leading zeroes. Return the resulting reversed number.

# Example 1:

# Input: 200
# Output: 2
# Explanation: By reversing the digits of 
# number, number will change into 2.

# Example 2:

# Input : 122
# Output: 221
# Explanation: By reversing the digits of 
# number, number will change into 221.


# Your Task:
# You don't need to read or print anything. Your task is to complete the function reverse_digit() which takes N as input parameter and returns the reversed number.
 

# Expected Time Complexity: O(Log(N))
# Expected Space Complexity: O(1)
 

# Constraints:
# 1 <= N <= 1015



def reverse_digit(digit):
    string_digit=str(digit) 
    index=len(string_digit)-1
    trailing=True
    i=0
    length=len(string_digit)/2
    while index>=length:
        letter=string_digit[index]
        if string_digit[index]=='0' and trailing:
           index-=1
           continue
        else:
            trailing=False
            string_digit[index]=string_digit[i]
            string_digit[i]=letter
            i+=1
            index-=1
    return int(string_digit)
            

if __name__=='__main__':
    digit=2233456
    print(reverse_digit(digit))
