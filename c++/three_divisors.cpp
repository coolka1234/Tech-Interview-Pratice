// You are given a list of q queries and for every query, you are given an integer N.  The task is to find how many numbers(less than or equal to N) have number of divisors exactly equal to 3.

// Example 1:

// Input:
// q = 1
// query[0] = 6
// Output:
// 1
// Explanation:
// There is only one number 4 which has
// exactly three divisors 1, 2 and 4 and
// less than equal to 6.

// Example 2:

// Input:
// q = 2
// query[0] = 6
// query[1] = 10
// Output:
// 1
// 2
// Explanation:
// For query 1 it is covered in the
// example 1.
// query 2: There are two numbers 4 and 9
// having exactly 3 divisors and less than
// equal to 10.

// Your Task:  
// You don't need to read input or print anything. Your task is to complete the function threeDivisors() which takes an integer q and a list of integer of size q as input parameter and returns the list containing the count of the numbers having exactly 3 divisors for each query.
// Expected Time Complexity: O(q*N*log(log(N)))
// Expected Auxiliary Space: O(N), where N is min(10^6,N)

#include <iostream>
#include <math.h>
void output_threes(int* queries, int size){
    int counter_of_non_primes=0;
    for(int i=0;i<size;i++){
        int N=queries[i];
        bool primes[int(sqrt(N))]={true};
        for(int j=2;j<sqrt(N);j++){
           int k=1;
           while(k*j<=sqrt(N)){
            if(primes[(k*j)-1]){
                primes[(k*j)-1]=false;
                counter_of_non_primes++;
            }
           }
        }
        int num_of_primes=N-counter_of_non_primes;

    }    
}
int main(){
   return 0; 
}