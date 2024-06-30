 #include<math.h>
#include <iostream>
 int maxOfArray(const int* A, int size)
 {
    int max=A[0];
    int size_A=sizeof(A);
    int size_int=sizeof(int);
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