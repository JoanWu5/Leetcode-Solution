# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        elif t1 is None or t2 is None:
            return t1 or t2
        else:
            root = TreeNode(t1.val+t2.val)
            left = self.mergeTrees(t1.left,t2.left)
            right = self.mergeTrees(t1.right,t2.right)
            root.left = left
            root.right = right
            return root

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.left.left = TreeNode(5)
t1.right = TreeNode(2)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.left.right = TreeNode(4)
t2.right = TreeNode(3)
t2.right.right = TreeNode(7)

s= Solution()
root = s.mergeTrees(t1,t2)

def print_Tree(root):
    if root:
        print(root.val)
        print_Tree(root.left)
        print_Tree(root.right)

print_Tree(root)

        