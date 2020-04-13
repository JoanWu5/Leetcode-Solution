class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sumdigits(n):
            result = 0
            while n>=1:
                digit = n%10
                result +=digit**2
                n = n//10
            return result
        all_possiblity = []
        while True:
            result = sumdigits(n)
            # print(result)
            if result == 1:
                return True
            elif result in all_possiblity:
                return False
            else:
                all_possiblity.append(result)
                n = result

s = Solution()
print(s.isHappy(19))