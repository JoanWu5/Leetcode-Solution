# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #vesion 1：	Time Limit Exceeded
        # if headA is None or headB is None:
        #     return None
        # cur = headB
        # while headA:
        #     while cur:
        #         if cur == headA
        #             return cur
        #         cur = cur.next
        #     headA = headA.next
        #     cur = headB        
        # return None

        #version 2 two pointers
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            if pb:
                pb = pb.next
            else:
                pb = headA
        return pa

        


                