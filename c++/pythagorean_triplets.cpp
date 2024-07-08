// Pythagorean Triples

// A Pythagorean triplet is a set of three numbers a, b, and c where a^2 + b^2 = c^2. In this Kata, you will be tasked with finding the Pythagorean triplets whose product is equal to n, the given argument to the function pythagorean_triplet.
// Your task

// In this Kata, you will be tasked with finding the Pythagorean triplets whose product is equal to n, the given argument to the function, where 0 < n < 10000000
// Examples

// One such triple is 3, 4, 5. For this challenge, you would be given the value 60 as the argument to your function, and then it would return the Pythagorean triplet in an array [3, 4, 5] which is returned in increasing order. 3^2 + 4^2 = 5^2 since 9 + 16 = 25 and then their product (3 * 4 * 5) is 60.
//CAN BE GREATLY IMPROVED! 
#include <iostream>
#include <math.h>
#include <vector>
#include <string>
std::vector<int> triplet(int num){
    std::vector<int> triplets={1,1,1};
    int sum=num;
    for (int i=1;i<num/2;i++){
        for(int j=1;j<=i;j++){
            for(int k=1;k<=i;k++){
                // std::cout<<i<<j<<k<<std::endl;
                if(pow(k,2)+pow(j,2)==pow(i,2) && (i * j * k)==num){
                    // std::cout<<"found triplet";
                    return (triplets={k,i,j});
                }
            }
        }
    }
    return triplets;

}
int main(){
    std::vector<int> result=triplet(2040); 
    std::cout<<result[0]<<" ";
    std::cout<<result[1]<<" ";
    std::cout<<result[2]<<" ";
    return 0;
}