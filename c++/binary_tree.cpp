#include <iostream>
#include <vector>

using namespace std;
template <typename T> 
class MyBinaryTree{
    private T currentNode;
    private T* parent;
    private T* lChild;
    private T* rChild;
    public:
    MyBinaryTree();
    MyBinaryTree(T arr[], int s);
    MyBinaryTree(vector<T> vec);
    void add(T elem);
    vector<T> bfs();

};