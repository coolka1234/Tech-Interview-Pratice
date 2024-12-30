#include <iostream>
#include <vector>

using namespace std;
template <typename T>
class Node{
private:
    Node<T> *parent;
    T current;
    Node<T> *left;
    Node<T> *right;
public:
    Node<T>();
    Node<T>(Node<T> *parent, Node<T> *left, Node<T>* right);
};
template <typename T> 
class MyBinaryTree{
    private:
    Node<T> root;
    public:
    MyBinaryTree();
    MyBinaryTree(T arr[], int s);
    MyBinaryTree(vector<T> vec);
    void add(T elem);
    vector<T> bfs();

 };

 template <typename T>
 MyBinaryTree<T>::MyBinaryTree(T arr[], int s){
    if(s<=0){
        return;
    }
    else{

    }    
 }

int main()
{
    return 0;
}