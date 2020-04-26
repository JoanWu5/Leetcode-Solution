# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        def pathSum2(root,sum,path,result):
            if root is None:
                return
            if root.left is None and root.right is None and root.val == sum:
                path.append(root.val)
                result.append(path)
            if root.left:
                pathSum2(root.left,sum-root.val,path+[root.val],result)
            if root.right:
                pathSum2(root.right,sum-root.val,path+[root.val],result)

        pathSum2(root,sum,[],result)
        return result
