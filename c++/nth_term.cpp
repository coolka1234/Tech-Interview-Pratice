// Given the first 2 terms a1 and a2 of an Arithmetic Series.Find the nth term of the series. 

// Example 1:

// Input:
// a1 = 2
// a2 = 3
// n = 4
// Output: 5
// Explanation:
// The series is: 2,3,4,5,6....
// Thus,4th term is 5.

// Example 2:

// Input:
// a1 = 1
// a2 = 3
// n = 10
// Output: 19
// Explanation:
// The series is: 1,3,5,7,9,11,13,15,17,19,21..
// Thus,10th term is 19.

// Your Task:
// You don't need to read input or print anything.Your Task is to complete the function nthTermOfAP() which takes three integers a1, a2 and n as input parameters and returns the nth term of the AP that has a1 and a2 as the first and second terms respectively.

// Expected Time Complexity:O(1)
// // Expected Auxillary Space:O(1)
#include <iostream>
#include <algorithm>
#include <math.h>
int nth_term(int first_term, int second_term, int n){
    int q=second_term-first_term;
    n=first_term+q*(n-1);
    return n;
}
int main(){
    std::cout<<nth_term(1,3,10);
    return 0;
}