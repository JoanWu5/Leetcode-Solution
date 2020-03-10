# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #version 1：递归法
        # if root is None:
        #     return []
        
        # def print_Inorder(result,root):
        #     if root != None:
        #         if root.left!=None:
        #             print_Inorder(result,root.left)
        #         result.append(root.val)
        #         if root.right!=None:
        #             print_Inorder(result,root.right)
        
        # result = []
        # print_Inorder(result,root)
        # return result

        #version 2:迭代法
        if root is None:
            return []
        stack = [(1,root)]
        result = []
        while stack:
            go_deeper, node = stack.pop()
            if node is None:
                continue
            if go_deeper:
                stack.append((1,node.right))
                stack.append((0,node))
                stack.append((1,node.left))
            else:
                result.append(node.val)

        return result

s = Solution()
root = TreeNode([1,None,2,3])
result = s.inorderTraversal(root)
print(result)
            
            