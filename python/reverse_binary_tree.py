# Given the root of a binary tree, invert the tree, and return its root.

def reverse(root, result=[]):
    root_len=len(root)
    if root_len<=2:
        return [root[1], root[0] + result]
    else:
        result+=reverse(root[2:root_len], [])
        

root = [4,2,7,1,3,6,9]
print(reverse(root))
