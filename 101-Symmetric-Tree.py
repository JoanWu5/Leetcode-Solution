# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #version 1:递归
        # def isSymmetric(left,right):
        #     if left is None and right is None:
        #         return True
        #     if left is None or right is None:
        #         return False
        #     return left.val == right.val and isSymmetric(left.right,right.left) and isSymmetric(left.left,right.right)

        # if root is None:
        #     return True
        # return isSymmetric(root,root)

        #version 2:迭代
        if root is None:
            return True
        stack = [[root.left,root.right]]
        while len(stack)>0:
            pair = stack.pop()
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0,[left.left,right.right])
                stack.insert(0,[left.right,right.left])
            else:
                return False
        return True

    
                
    