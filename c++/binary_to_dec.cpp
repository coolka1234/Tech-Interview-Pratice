// Given a Binary Number B, find its decimal equivalent.

// Example 1:

// Input: B = 10001000
// Output: 136

// Example 2:

// Input: B = 101100
// Output: 44

// Your Task:
// You don't need to read or print anything. Your task is to complete the function binary_to_decimal() which takes the binary number as string input parameter and returns its decimal equivalent. 

// Constraints:
// 1 <= number of bits in binary number  <= 16
#include <iostream>
#include <string>
int bin_to_dec(std::string dec){
    int result=0;
    int pow=0;
    for(int i=dec.size()-1;i>=0;i--)
    {
        if(dec[i]=='1'){
            result+=2^pow;
        }
        pow++;
    }
    return result;

}
int main(){
    std::string num="1000101011";
    std::cout<<bin_to_dec(num);
    return 0;
}