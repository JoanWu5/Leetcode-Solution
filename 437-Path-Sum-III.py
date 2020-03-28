# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.pathhelper(root,[],[],sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        return 0

    def pathhelper(self,root,path,pathsum,target):
        result = 0
        if root:
            path.append(root.val)
            if root.val == target:
                result +=1
                pathsum.append(path.copy())
            print(pathsum)
            result +=self.pathhelper(root.left,path,pathsum,target-root.val)
            result +=self.pathhelper(root.right,path,pathsum,target-root.val)
        return result
        # if root:
        #     return int(root.val == target) + self.pathhelper(root.left,target-root.val)+self.pathhelper(root.right,target-root.val)
        # return 0

        

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)

s = Solution()
print(s.pathSum(root,3))


        