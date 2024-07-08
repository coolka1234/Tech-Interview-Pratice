// Print a sequence of numbers starting with nn, without using a loop. Replace nn with n−5n - 5n−5 until n≤0n \leq 0n≤0. Then, replace n with n+5n + 5n+5 until nn regains its initial value. Complete the function pattern(n) which takes n as input and returns a list containing the pattern.

// Examples

// Input: n = 16
// Output: 16 11 6 1 -4 1 6 11 16
// Explanation: The value decreases until it is greater than 0. After that it increases and stops when it becomes 16 again.

// Input: n = 10
// Output: 10 5 0 5 10
// Explanation: It follows the same logic as per the above example.

// Expected Time Complexity: O(n)
// Expected Auxiliary Space: O(n)

// Constraints:
// -105 ≤ n ≤ 105
#include <iostream>
void print_pattern(int number, int orginal_number, bool first_iter, bool ifFlipped){
    if (number==orginal_number && !first_iter){
        std::cout<<number<<" ";
        return;
    }
    std::cout<<number<<" ";
    if (number>0 && !ifFlipped){
        print_pattern(number-5, orginal_number=orginal_number, first_iter=false, ifFlipped=false);
    }
    else{
      print_pattern(number+5, orginal_number=orginal_number, first_iter=false, ifFlipped=true);  
    }
}
int main(){
    print_pattern(16, 16, true, false);
    return 0;
}