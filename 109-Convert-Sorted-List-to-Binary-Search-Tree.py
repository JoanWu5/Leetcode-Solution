# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        slow,fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        root = TreeNode(temp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)
        return root