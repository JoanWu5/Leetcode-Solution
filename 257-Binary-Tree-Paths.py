# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        def binaryTreePath2(root,path,result):
            if root:
                if root.left is None and root.right is None:
                    path += str(root.val)
                    result.append(path)
                else:
                    binaryTreePath2(root.left,path+str(root.val)+'->',result)
                    binaryTreePath2(root.right,path+str(root.val)+'->',result)
        binaryTreePath2(root,'',result)
        return  result