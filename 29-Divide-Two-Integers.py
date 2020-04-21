class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend<0) == (divisor<0)
        result = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend>=divisor:
            temp = divisor
            i = 1
            while dividend>=temp:
                dividend -=temp
                result +=i
                i<<=1
                temp<<=1
        if not sign:
            result = -result
        return min(max(-pow(2,31),result),pow(2,31)-1)

s = Solution()
print(s.divide(7,-3))