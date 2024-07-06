// Given a string str, convert the first letter of each word in the string to uppercase. 

// Example 1:

// Input:
// str = "i love programming"
// Output: "I Love Programming"
// Explanation:
// 'I', 'L', 'P' are the first letters of 
// the three words.


// Your Task:  
// You dont need to read input or print anything. Complete the function transform() which takes s as input parameter and returns the transformed string.


// Expected Time Complexity: O(N)
// Expected Auxiliary Space: O(N) to store resultant string  


// Constraints:
// 1 <= N <= 104
// The original string str only consists of lowercase alphabets and spaces to separate words
#include <iostream>
#include <cctype>
using namespace std;
string capitalize(string input){
    bool if_space=false;
    string result="";
    result+=toupper(input[0]);
    for (int i=1;i<input.size();i++){
        if(input[i]==' '){
            if_space=true;
        }
        else if(if_space){
            result+=toupper(input[i]);
            if_space=false;
            continue;   
        }
        result+=input[i];

    }
    return result;
}
int main(){
    cout<<capitalize("i love programming");
    return 0;
}