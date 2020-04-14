from collections import Counter
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        table = Counter(a+b for a in A for b in B)
        return sum(table[-c-d] for c in C for d in D)

s = Solution()
print(s.fourSumCount(A = [ 1, 2],B = [-2,-1],C = [-1, 2],D = [ 0, 2]))