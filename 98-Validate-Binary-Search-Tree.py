# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    #version 1:
    #     return self.helper(root)
        inorder = []
        inorder = self.create_inorder(root,inorder) 
        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True 

    # def helper(self,root,lower = float('-inf'),upper= float('inf')):
    #     if root:
    #         if root.val <=lower or root.val >=upper:
    #             return False
    #         if not self.helper(root.left,lower,root.val):
    #              return False
    #         if not self.helper(root.right,root.val,upper):
    #             return False
    #     return True

    #version2: inorder
    def create_inorder(self,root,inorder):
        if root:
            left = root.left
            right = root.right
            inorder = self.create_inorder(left,inorder)
            inorder.append(root.val)
            inorder = self.create_inorder(right,inorder)
        return inorder
    




root = TreeNode(1)
root.left = TreeNode(1)


s =Solution()
print(s.isValidBST(root))

        