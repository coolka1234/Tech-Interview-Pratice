package java_ti;


// Given a N x N matrix M. Write a program to find count of all the distinct elements common to all rows of the matrix. Print count of such elements.

// Example 1:

// Input: 
// N = 4
// M = {{2, 1, 4, 3},
//      {1, 2, 3, 2},
//      {3, 6, 2, 3},
//      {5, 2, 5, 3}}
// Output: 
// 2
// Explaination: Only 2 and 3 are common in all rows.

// Example 2:

// Input: 
// N = 5
// M = {{12, 1, 14, 3, 16},
//      {14, 2, 1, 3, 35},
//      {14, 1, 14, 3, 11},
//      {14, 5, 3, 2, 1},
//      {1, 18, 3, 21, 14}}
// Output: 
// 3
// Explaination: 14, 3 and 1 are common in all the rows.

// Your Task:
// You do not need to read input or print anything. Your task is to complete the function distinct() which takes the matrix and n as input parameters and returns the number of distinct elements present in every row.

// Expected Time Complexity: O(N*N)
// Expected Auxiliary Space: O(N)

// Constraints:
// 1 ≤ N ≤ 100
// 1 ≤ M[i][j] ≤ 1000
import java.util.HashSet;

class distinct_matrixes {
    public static void main(String args[]) {
        int[][] matrix={
      {12, 1, 14, 3, 16},
      {14, 2, 1, 3, 35},
      {14, 1, 14, 3, 11},
      {14, 5, 3, 2, 1},
      {1, 18, 3, 21, 14}};
      System.out.println(is_distinc(matrix));

    }

    public static int is_distinc(int[][] matrix) {
        HashSet<Integer> set_of_num = new HashSet<>();
        HashSet<Integer> next_sum=new HashSet<>();
        boolean first=true;
        for (int[] list : matrix) {
            for (int element : list) {
                if (first){
                    set_of_num.add(element);
                }
                else{
                    if(set_of_num.contains(element)){
                        next_sum.add(element);
                        
                    }
                }
            }
            if (first)
            {
                next_sum=set_of_num;
                first=false;
            }
            else{
                set_of_num=next_sum;
                next_sum=new HashSet<>();
            }
        }
        return set_of_num.size();
    }
}
