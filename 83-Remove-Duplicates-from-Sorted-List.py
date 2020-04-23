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
        number = []
        dummy = ListNode(0)
        cur = dummy
        while head:
            if head.val not in number:
                number.append(head.val)
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return dummy.next

s = Solution()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
new = s.deleteDuplicates(head)
while new:
    print(new.val)
    new = new.next