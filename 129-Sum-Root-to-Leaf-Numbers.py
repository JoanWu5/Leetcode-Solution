# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        def binaryTreePath(root,path,result):
            if root:
                if root.left is None and root.right is None:
                    path += str(root.val)
                    result.append(path)
                else:
                    binaryTreePath(root.left,path+str(root.val),result)
                    binaryTreePath(root.right,path+str(root.val),result)
        result = []
        binaryTreePath(root,'',result)
        sum1 = 0
        for i in range(len(result)):
            sum1+=int(result[i])
        return sum1