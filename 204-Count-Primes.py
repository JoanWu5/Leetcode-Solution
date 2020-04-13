import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #version 1:Time Limit Exceeded
        # def isPrime(n):
        #     for i in range(2,int(math.sqrt(n))+1):
        #         if n%i == 0:
        #             return False
        #     return True
        
        # if n <=2:
        #     return 0
        # count = 0
        # for i in range(2,n):
        #     if isPrime(i):
        #         # print(i)
        #         count +=1
        # return count

        #version 2:
        if n<=2:
            return 0
        result = [True]*n
        result[0] = result[1] = False
        for i in range(2,n):
            if result[i]:
                for j in range(2,(n-1)//i+1):
                    result[i*j] = False
        return sum(result)

s = Solution()
print(s.countPrimes(10))
        