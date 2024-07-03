// You are given a number n. You need to print the pattern for the given value of n.

// For n = 2 the pattern will be 
// 2 2 1 1
// 2 1

// For n = 3 the pattern will be 
// 3 3 3 2 2 2 1 1 1
// 3 3 2 2 1 1
// 3 2 1

// Note: Instead of printing a new line print a "$" without quotes. After printing the total output, end of the line("$") is expected.

// Examples :

// Input: 2
// Output: 2 2 1 1 $2 1 $

// Input: 3
// Output: 3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $


// Constraints:
// 1 <= n <= 40
#include <iostream>

void print_pattern(int n){
    for (int k=n;k>0;k--){
        for (int i=n;i>0;i--){
            for (int j=k;j>0;j--){
                std::cout<<i<<" ";
            }
        }
        std::cout<<"$";
    }
}
int main(){
    print_pattern(40);
}