// For a given number n check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.

// Examples :

// Input: n = 5
// Output: 1
// Explanation: 5 has 2 factors 1 and 5 only.

// Input: n = 25
// Output: 0
// Explanation: 25 has 3 factors 1, 5, 25

// Your Task:
// You don't need to read input or print anything. Your task is to complete the function isPrime() which takes an integer n as input parameters and returns an integer, 1 if n is a prime number or 0 otherwise.

// Expected Time Complexity: O(sqrt(n))
// Expected Space Complexity: O(1)

// Constraints:
// 1 <= n <= 109
#include <iostream>
bool isPrime(int number){

    for(int i=2;i*i<number;i++){
        if(number%i==0){
            return false;
        }
    }
    return true;
}

int main(){
    int number=31;
    std::cout<<isPrime(number)<<std::endl;
    return 0;
}