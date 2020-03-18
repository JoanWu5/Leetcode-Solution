import sys
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #version 1 :DP
        # dp = [sys.maxsize]*(n+1)
        # dp[0] = 0
        # for i in range(1,n+1):
        #     for j in range(1,int(math.sqrt(i))+1):
        #         dp[i] = min(dp[i],dp[i-j*j]+1)
        # return dp[n]

        #version2 :BFS
        square = [i*i for i in range(1,int(math.sqrt(n)+1))]
        print(square)
        level = 0
        currentLevel = [0]
        while True:
            nextLevel = []
            for i in currentLevel:
                for j in square:
                    if i+j ==n:
                        return level+1
                    if i+j<n:
                        nextLevel.append(i+j)
            currentLevel = list(set(nextLevel))
            level +=1


s = Solution()
result = s.numSquares(12)
print(result)

