// Given a positive integer, n. Find the factorial of n.

// Examples :

// Input: n = 5
// Output: 120
// Explanation: 5*4*3*2*1 = 120

// Input: n = 4
// Output: 24
// Explanation: 4*3*2*1 = 24 

// Constraints:
// 0 <= n <= 18
#include <iostream>

long long factorial(int n){
    long long result=1;
    for (int i = 2; i <= n; i++)
    {
        result=result*i;
    }
    return result;
    

}
int main(){
    std::cout<<factorial(5);
    return 0;
}
