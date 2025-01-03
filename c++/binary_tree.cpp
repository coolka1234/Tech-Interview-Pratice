#include <iostream>
#include <vector>
#include <queue>

using namespace std;
template <typename K> 
class MyBinaryTree{
    private:
    class Node{
    protected:
        Node *parent;
        K current;
        Node *left;
        Node *right;
    public:
        Node();
        Node(Node *parent, Node *left, Node* right);
        friend class MyBinaryTree;
    };

    Node root;
    public:
    MyBinaryTree();
    MyBinaryTree(K arr[], int s);
    MyBinaryTree(vector<K> vec);
    void add(K elem);
    vector<K> bfs();

 };
 template <typename K>
 MyBinaryTree<K>::Node::Node(){
    current=NULL;
    this->left=nullptr;
    this->right=nullptr;
 }

 template <typename K>
 MyBinaryTree<K>::MyBinaryTree(K arr[], int s){
    if(s<=0){
        return;
    }
    else{
        MyBinaryTree::root.current=arr[0];
        MyBinaryTree::Node currNode=root;
        currNode.parent=nullptr;
        currNode.current=arr[0];
        currNode.left=nullptr;
        currNode.right=nullptr;
        MyBinaryTree::Node* leftMost=nullptr;
        for (int i=1;i<s;i++){
            if(currNode.left==nullptr){
                (currNode.left)->current=arr[i];
                leftMost=currNode.left;
            }
            else if(currNode.right==nullptr){
                (currNode.right)->current=arr[i];
            }
            else if(currNode.parent!=nullptr && currNode.parent->right==nullptr){
                (currNode.parent->right)->current=arr[i];
                currNode=* (currNode.parent->right);
            }
            else{
                currNode=*leftMost;
            }
        }
    }    
    cout<<"Constructed tree"<<endl;
 }
template <typename K>
vector<K> MyBinaryTree<K>::bfs(){
    queue<Node> bsfQueue;
    vector<K> result;
    if(root.current!=NULL){
        bsfQueue.push(root);
        result.push_back(root.current);
    }
    while(!bsfQueue.empty()){
        Node n=bsfQueue.front();
        bsfQueue.pop();
        if(n.left!=nullptr){
        if(find(result.begin(), result.end(), *n.left)!=result.end()){
            result.push_back(*n.left);
            bsfQueue.push(*n.left);
        }
        }
        if(n.right!=nullptr){
        if(find(result.begin(), result.end(), *n.right)!=result.end()){
            result.push_back(*n.right);
            bsfQueue.push(*n.right);
        }
        }
        
        
    }


}

int main()
{
    int arr[9]={1,2,3,4,5,6,7,8,9};
    cout<<"main"<<endl;
    MyBinaryTree<int> tree=MyBinaryTree<int>(arr, 9);
    return 0;
}