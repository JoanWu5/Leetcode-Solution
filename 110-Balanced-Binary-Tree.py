# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def maxdepth(root):
            depth = 0
            if root is None:
                return 0
            depth+=1
            left = maxdepth(root.left)
            right =maxdepth(root.right)
            depth+=max(left,right)
            return depth

        if root is None:
            return True
        else:
            left = maxdepth(root.left)
            right = maxdepth(root.right)
            if abs(left-right)>1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)


        