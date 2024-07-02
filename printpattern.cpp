#include <iostream>

void print_pattern(int n){
    for (int k=n;k>0;k--){
        for (int i=n;i>0;i--){
            for (int j=k;j>0;j--){
                std::cout<<i<<" ";
            }
        }
        std::cout<<"$";
    }
}
int main(){
    print_pattern(3);
}