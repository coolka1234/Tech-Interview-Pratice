
# Given the root of a binary tree, invert the tree, and return its root.
#
#
#
# Example 1:
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
import queue

class Node():
    def __init__(self, right, left, value):
        self.value=value
        self.right=right
        self.left=left

    def __str__(self):
        return (f"value {self.value}, right {self.right}, left {self.left}")

class BinaryTree():
    def __init__(self, root: Node):
        self.root=root

    def __str__(self):
        result=[]
        que=queue.Queue()
        que.put(self.root)
        while not que.empty():
            inspected=que.get()
            result.append(inspected.value)
            if (inspected.left is not None):
                que.put(inspected.left)
            if (inspected.right is not None):
                que.put(inspected.right)
        return str(result)
    def bfs(self):
        result=[]
        que=queue.Queue()
        que.put(self.root)
        while not que.empty():
            inspected=que.get()
            result.append(inspected.value)
            if (inspected.left is not None):
                que.put(inspected.left)
            if (inspected.right is not None):
                que.put(inspected.right)
        return result
    def dfs(self):
        def visit_node(node: Node, visited: set, result):
            if node.left is not None and node.left not in visited:
                visited.add(node.left)
                result.append(node.left.value)
                visit_node(node.left, visited, result)
            if node.right is not None and node.right not in visited:
                visited.add(node.right)
                result.append(node.right.value)
                visit_node(node.right, visited, result)
        result=[]
        visited=set()
        result.append(self.root.value)
        visited.add(self.root)
        if self.root.left is not None:
            result.append(self.root.left.value)
            visited.add(self.root.left)
            visit_node(self.root.left, visited, result)
        if self.root.right is not None:
            result.append(self.root.right.value)
            visited.add(self.root.right)
            visit_node(self.root.right, visited, result)
        return result



    def invert(self):
        que=queue.Queue()
        que.put(self.root)
        while not que.empty(): 
            current=que.get()
            current.left, current.right = current.right, current.left
            if(current.left is not None):
                que.put(current.left)
            if(current.right is not None):
               que.put(current.right)


    def is_same(self, other):
        return self.bfs() == other.bfs()



n1=Node(None, None, 1)
n2=Node(None, None, 2)
n3=Node(None, None, 3)
n4=Node(None, None, 4)
n5=Node(n1, n2, 5)
n6=Node(n4, n3, 6)
root=Node(n5,n6, 7)
b_tree=BinaryTree(root)

n1=Node(None, None, 1)
n2=Node(None, None, 3)
n3=Node(None, None, 3)
n4=Node(None, None, 4)
n5=Node(n1, n2, 5)
n6=Node(n4, n3, 8)
root=Node(n5,n6, 7)
b2_tree=BinaryTree(root)
# print(str(b_tree))

# b_tree.invert()

# print(str(b_tree))

# print(b_tree.is_same(b_tree))
# print(b2_tree.dfs())
print(b_tree.dfs())

