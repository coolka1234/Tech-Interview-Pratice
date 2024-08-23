// Given a alphanumeric string S, extract maximum numeric value from S.

// Example 1:

// Input:
// S = 100klh564abc365bg
// Output: 564
// Explanation: Maximum numeric value 
// among 100, 564 and 365 is 564.

// Example 2:

// Input:
// S = abcdefg
// Output: -1
// Explanation: Return -1 if no numeric 
// value is present. 


// Your Task:  
// You dont need to read input or print anything. Complete the function extractMaximum() which takes the string S as input parameters and returns the maximum numeric value. If it is not present in S, return -1.

 

// Expected Time Complexity: O(|S|)
// Expected Auxiliary Space: O(1)

 

// Constraints:
// 1 ≤ |S| ≤ 104
// -1 ≤ output value ≤ 106
#include <iostream>

int max_value(std::string S){
    int max=-1;
    int s_size=S.size();
    std::string result_string="";
    for(int i=0;i<s_size;i++){
        int c=S[i]-'0';
        if (c>=47 && c<=57){
            result_string+=S[i];
        }
        else{
            int result=std::stoi(result_string);
            if (result>max){
                max=result;
            }
            result_string="";
        }
    }    
}

int main(){

}