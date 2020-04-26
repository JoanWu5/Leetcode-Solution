"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        p = root
        while p:
            cur = p
            head = prev = Node(0)
            while cur:
                if cur.left:
                    prev.next = cur.left
                    prev = cur.left
                if cur.right:
                    prev.next = cur.right
                    prev = cur.right
                cur = cur.next
            p = head.next
        return root
            