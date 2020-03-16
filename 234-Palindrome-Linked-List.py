# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #version 1:Time Limit Exceeded
        # if head is None or head.next is None:
        #     return True
        # cur = head
        # while cur.next.next:
        #     cur = cur.next
        # if head.val != cur.next.val:
        #     return False
        # else:
        #     cur.next = None
        #     return self.isPalindrome(head.next)

        #version 2:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
        




