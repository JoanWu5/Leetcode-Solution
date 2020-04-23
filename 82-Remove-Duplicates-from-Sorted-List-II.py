# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # number = {}
        # cur = head
        # while cur:
        #     if cur.val in number:
        #         number[cur.val] +=1
        #     else:
        #         number[cur.val] =1
        #     cur = cur.next
        # dummy = ListNode(0)
        # cur = dummy
        # while head:
        #     if number[head.val] == 1:
        #         cur.next = head
        #         cur = cur.next
        #     head = head.next
        # cur.next = None
        # return dummy.next
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next
  