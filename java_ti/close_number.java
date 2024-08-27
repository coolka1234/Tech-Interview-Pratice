package java_ti;

// Given  two integers N and M. The problem is to find the number closest to N and divisible by M. If there are more than one such number, then output the one having maximum absolute value.

 

// Example 1:

// Input:
// N = 13 , M = 4
// Output:
// 12
// Explanation:
// 12 is the Closest Number to
// 13 which is divisible by 4.

// Example 2:

// Input:
// N = -15 , M = 6
// Output:
// -18
// Explanation:
// -12 and -18 are both similarly close to
// -15 and divisible by 6. but -18 has
// the maximum absolute value.
// So, Output is -18

 

// Your Task:
// You don't need to read input or print anything. Your task is to complete the function closestNumber() which takes an Integer n as input and returns the answer.

 

// Expected Time Complexity: O(1)
// Expected Auxiliary Space: O(1)
class close_number{
    public static void main(String args[]){
        System.out.println(closest_number(-60, 18));
        System.out.println(-60%18);
    }
    public static int closest_number(int num, int div){
        int close_number;
        int rest=(num%div);
        int close_number_1=num+rest;
        int close_number_2=num-rest;
        boolean firstdiv=close_number_1%div==0;
        boolean seconddiv=close_number_2%div==0;
        if (firstdiv && !seconddiv){
            return close_number_1;
        }
        else if(!firstdiv && seconddiv){
            return close_number_2;
        }
        else{
        close_number=Math.max(Math.abs(close_number_1),Math.abs(close_number_2));
        return close_number;
        }
    }
}