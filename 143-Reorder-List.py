# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        slow= head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second =slow.next
        slow.next = None
        dummy = ListNode(0)
        dummy.next = cur = second
        while cur:
            temp = cur.next
            cur.next = dummy
            dummy = cur
            cur = temp
        dummy2 = cur = ListNode(0)
        cur1 = head
        cur2 = dummy
        count = 0
        while cur1:
            if count%2 == 0:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
            count+=1
        if cur2 and cur2.val!=0:
            cur.next = cur2
            cur2.next = None
        return dummy2.next
        