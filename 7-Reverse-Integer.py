class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x is None:
        #     return None
        # if x == 0 or x == -0:
        #     return 0
        # x = str(x)
        # result = ''
        # sign = ''
        # flag = 0
        # if x[0] == '-':
        #     sign = '-'
        #     flag = 1
        # x = list(reversed(x))
        # i = 0
        # while x[i] == '0':
        #     i +=1
        # result = sign + ''.join(x[i:len(x)-flag])
        # result = int(result)
        # if  result<-pow(2,31) or result>pow(2,31)-1:
        #     result = 0
        # return result
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0


s = Solution()
print(s.reverse(-10))
print([1,-1][1])



        

        