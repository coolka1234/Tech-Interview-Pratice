// Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

// Examples:

// Input: arr[] = [10, 20, 30, 40, 50]
// Output: true
// Explanation: The given array is sorted.

// Input: arr[] = [90, 80, 100, 70, 40, 30]
// Output: false
// Explanation: The given array is not sorted.

// Expected Time Complexity: O(n)
// Expected Auxiliary Space: O(1)

// Constraints:
// 1 ≤ arr.size ≤ 106
// - 109 ≤ arr[i] ≤ 109
package java;

import java.util.ArrayList;

public class is_sorted {
    public static Boolean sorted(ArrayList<Integer> arr){
        int number=arr.get(0);
        int counter=0;
        for (Integer num : arr) {
            if (counter==0){
                continue;
            }
            else if(num>number){
                return false;
            }
            number=num;
        }
        return true;
    }
    public static void main(String args[]){

    }
    
}
