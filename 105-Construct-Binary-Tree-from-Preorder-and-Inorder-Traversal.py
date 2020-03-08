# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) <= 0:
            return None
        else:
            root = TreeNode(preorder[0])
            n = inorder.index(root.val)
            root.left = self.buildTree(preorder[1:n+1],inorder[0:n])
            root.right = self.buildTree(preorder[n+1:],inorder[n+1:])
            return root

    def printTree(self,tree):
        if not tree is None:
            print(tree.val)
            left = tree.left
            self.printTree(left)
            right = tree.right
            self.printTree(right)

s = Solution()
tree = s.buildTree(preorder = [3,9,20,15,7],inorder = [9,3,15,20,7])
s.printTree(tree)