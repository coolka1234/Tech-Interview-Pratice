// Given an array arr of positive integers and another number x. Determine whether two elements exist in arr whose sum is exactly x or not.

// Examples:

// Input: x = 16, arr[] = [1, 4, 45, 6, 10, 8]
// Output: true
// Explanation: arr[3] + arr[4] = 6 + 10 = 16

// Input: x = 11, arr[] = [1, 2, 4, 3, 6]
// Output: false
// Explanation: None of the pair makes a sum of 11

// Expected Time Complexity: O(n)
// Expected Auxiliary Space: O(n)


class key_pair{
    public static void main(String args[]){
        int[] array={1,4,45,6,10,8};
        System.out.println(sum_exists(array,14));

    }
    //not optimal - n^2!
    public static Boolean sum_exists(int arr[], int sum){
        int copy[]=arr;
        for (int i=0;i<arr.length;i++){
            for (int j=0;j<=i;j++){
                int sum_of=copy[j]+arr[i];
                if (sum_of==sum){
                    return true;
                }
            }
        }
        return false;
    }
}