# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
    #     result = []
    #     self.create_list(root,result)
    #     return result[k-1]

    # def create_list(self,root,result):
    #     if root:
    #         self.create_list(root.left,result)
    #         result.append(root.val)
    #         self.create_list(root.right,result)

        result = [k]
        self.findNode(root,result)
        return result[1]

    def findNode(self,node,result):
        if len(result)>1:
            return
        if node.left:
            self.findNode(node.left,result)
        result[0]-=1
        if result[0]==0:
            result.append(node.val)
            return
        if node.right:
            self.findNode(node.right,result)
        