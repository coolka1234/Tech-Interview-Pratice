// Given two numbers as strings s1 and s2. Calculate their Product.

// Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

// Example 1:

// Input:
// s1 = "0033"
// s2 = "2"
// Output:
// 66

// Example 2:

// Input:
// s1 = "11"
// s2 = "23"
// Output:
// 253

// Your Task: You don't need to read input or print anything. Your task is to complete the function multiplyStrings() which takes two strings s1 and s2 as input and returns their product as a string.
#include <iostream>
using namespace std;
int multiply_string(string s1, string s2){
    char signs[2]={s1[0],s2[0]};
    bool negative_product=false;
    if(signs[0]=='-' || signs[1]=='-'){
        negative_product = (signs[0]!=signs[1]);
    }
    int l1=s1.size();
    int l2=s2.size();
    if (l1<l2){
        swap(s1,s2);
        swap(l1,l2);
    }
    for(int i=l1-1;i>=0;i--){
        int first_num=s1[i];
        for(int j=l2-1;j>=0;j--){

        }        
    }          
}

int main(){
    return 0;
}
