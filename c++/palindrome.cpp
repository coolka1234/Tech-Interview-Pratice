// Given a string S, check if it is palindrome or not.

// Example 1:

// Input: S = "abba"
// Output: 1
// Explanation: S is a palindrome

// Example 2:

// Input: S = "abc" 
// Output: 0
// Explanation: S is not a palindrome

// Your Task:
// You don't need to read input or print anything. Complete the function isPalindrome()which accepts string S and returns an integer value 1 or 0.

// Expected Time Complexity: O(Length of S)
// Expected Auxiliary Space: O(1)

// Constraints:
// 1 <= Length of S<= 2*105
#include <iostream>
bool isPalindrome(std::string S){
    int size=S.size();
    for(int i=0;i<size/2;i++)
    {
        if(S[i]!=S[i-1]){
            return false;
        }
    }
    return true;
}
int main(){
    std::string test_s="abba";
    std::cout<<isPalindrome(test_s)<<std:endl;
}