// See https://aka.ms/new-console-template for more information
using System;
namespace Program{
    class Program{
        static void Main(string[] args){
                printCbrt(1000);
                System.Console.WriteLine("Bubble Sort");
                int[] arr = bubble_sort();
                for (int i = 0; i < arr.Length; i++){
                    Console.Write(arr[i] + " ");
                }
            }
        public static void printCbrt(int N){
            for (int i = 1; i <= N; i++){
                for (int j = 0; j <= N; j++){
                    if (i * i * i + j * j * j == N){
                        Console.WriteLine("Cbrt of " + N + " is " + i + " and " + j);
                        return;
                    }


                }
            }

        }
        public static int[] bubble_sort(){
            int[] arr = { 64, 34, 25, 12, 22, 11, 90 };
            int n = arr.Length;
            for (int i = 0; i < n - 1; i++){
                for (int j = 0; j < n - i - 1; j++){
                    if (arr[j] > arr[j + 1]){
                        int temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
            return arr;
        }
   }


}

