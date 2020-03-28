# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        elif root.left or root.right:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left,root.right = root.right,root.left
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

s = Solution()
newRoot = s.invertTree(root)

def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)

printTree(newRoot)


        
            
