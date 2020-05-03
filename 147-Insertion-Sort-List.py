# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        cur = head
        while cur:
            p = dummy
            while p.next and p.next.val<=cur.val:
                p = p.next
            temp = p.next
            p.next = cur
            cur= cur.next
            p.next.next = temp
        return dummy.next
        