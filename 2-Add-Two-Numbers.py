# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        flag = 0
        while l1 and l2:
            sum1= l1.val+l2.val+flag
            carry = sum1%10
            flag = sum1//10
            cur.next  = ListNode(carry)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        if l1 or l2:
            left = l1 or l2
            while left:
                sum1= left.val+flag
                carry = sum1%10
                flag = sum1//10
                cur.next  = ListNode(carry)
                cur = cur.next
                left = left.next
        if flag:
            cur.next = ListNode(1)
        return dummy.next