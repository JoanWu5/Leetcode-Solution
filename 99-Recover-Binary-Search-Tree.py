# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        cur,prev,drops,stack= root,TreeNode(float('-inf')),[],[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.val<prev.val:
                drops.append((prev,node))
            prev,cur = node,node.right
        drops[0][0].val,drops[-1][1].val = drops[-1][1].val,drops[0][0].val
                        
