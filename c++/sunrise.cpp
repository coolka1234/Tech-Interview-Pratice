// Given an array H representing heights of buildings. You have to count the buildings which will see the sunrise (Assume : Sun rise on the side of array starting point).
// Note : Height of building should be strictly greater than height of buildings in left in order to see the sun.

// Example 1:

// Input: 
// N = 5
// H[] = {7, 4, 8, 2, 9}
// Output: 3
// Explanation: As 7 is the first element, it
// can see the sunrise. 4 can't see the
// sunrise as 7 is hiding it.  8 can see.
// 2 can't see the sunrise. 9 also can see
// the sunrise.

// Example 2:

// Input: 
// N = 4
// H[] = {2, 3, 4, 5}
// Output: 4
// Explanation: As 2 is the first element, it
// can see the sunrise.  3 can see the
// sunrise as 2 is not hiding it. Same for 4
// and 5, they also can see the sunrise.

// Your Task:  
// You don't need to read input or print anything. Your task is to complete the function countBuildings() which takes the array of integers h and n as parameters and returns an integer denoting the answer.

// Expected Time Complexity: O(N)
// Expected Auxiliary Space: O(1)

// Constraints:
// 1 ≤ N ≤ 106
// 1 ≤ Hi ≤ 108
#include <iostream>
int count_buildings(int *arr, int size){
    // int size_of_buildings=sizeof(&arr)/sizeof(int);
    int count=0;
    int blockade=0;
    for (int i=0;i<size;i++){
        if(arr[i]>blockade){
            blockade=arr[i];
            count++;
        }
    }
    return count;
}

int main(){
    int array[6]={2,3,4,5,1,3};
    std::cout<<count_buildings(array, 6);
    return 0;
}