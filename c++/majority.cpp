// Problem Description
 
 
// Given an array of size N, find the majority element. The majority element is the element that appears more than floor(N/2) times.

// You may assume that the array is non-empty and the majority element always exist in the array.


// Problem Constraints
// 1 <= |A| <= 106
// 1 <= Ai <= 109


// Input Format
// The first argument is an integer array A.


// Output Format
// Return the majority element.
 #include<math.h>
#include <iostream>
 int maxOfArray(const int* A, int size)
 {
    int max=A[0];
    for (int i=0;i<size; i++)
    {
        if(max<A[i])
        {
            max=A[i];
        }
    }
    return max;
 }
 int majorityElement(const int* A, int n1) {
    int majority_elem=floor(n1/2);
    int max_size=maxOfArray(A, n1);
    int table_of_occurance[max_size]={ };
    for (int i=0;i<n1/2;i++)
    {
        table_of_occurance[(A[i])]++;
    }
    for (int i=n1/2;i<n1;i++)
    {
        table_of_occurance[A[i]]++;
        int potential=maxOfArray(table_of_occurance, max_size);
        if(potential>majority_elem)
        {
            return potential;
        }
    }
    return 0;
}
     
int main()
{
    int array[10]={6,1,6,6,6,8,7,6,15,6};
    std::cout<<"majority: "<<majorityElement(array,10)<<std::endl;
    return 0;
}