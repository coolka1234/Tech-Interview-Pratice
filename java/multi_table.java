package java;

// Create the multiplication table of a given number N and return the table as an array.


// Example 1:

// Input:
// N = 9

// Output:
// 9 18 27 36 45 54 63 72 81 90

// Explanation:
// The table of 9 is the output whose 1st 
// term is 9 and the 10th term is 90.


// Example 2:

// Input:
// N = 2

// Output:
// 2 4 6 8 10 12 14 16 18 20


// Your Task:  
// You don't need to read input. Your task is to complete the function getTable() which takes an integer N as input parameter and returns a list of integers denoting the multiplication of table of N from 1 to 10. 

// Expected Time Complexity: O(1)
// Expected Auxiliary Space: O(1)
class multi_table {
    public static void main(String[] args) {
        int[] table=print_multiples(9);
        for (int elem : table) {
            System.out.println(elem);
        }

    }
    public static int[] print_multiples(int n){
        int[] table = new int[10];
        for (int i=1;i<=10;i++){
            table[i-1]=n*i;
        } 
        return table;
    }
}
