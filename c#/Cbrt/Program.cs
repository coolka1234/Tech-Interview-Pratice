// See https://aka.ms/new-console-template for more information
using System;
namespace Program{
    class Program{
        static void Main(string[] args){
                printCbrt(1000);
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
   }


}

