
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


n1=Node(None, None, 1)
n2=Node(None, None, 2)
n3=Node(None, None, 3)
n4=Node(None, None, 4)
n5=Node(n1, n2, 5)
n6=Node(n4, n3, 6)
root=Node(n5,n6, 7)
b_tree=BinaryTree(root)

print(str(b_tree))


