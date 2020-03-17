# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        slow = head 
        fast = head.next
        while slow !=fast:
            if fast is None or fast.next is None:
                return None
            else:
                slow = slow.next
                fast = fast.next.next
        slow = slow.next
        while head!= slow:
            head = head.next
            slow = slow.next
        return head