import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        n = len(triangle[-1])
        dp = [[sys.maxsize for j in range(n)]for i in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1,m):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j]+triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
        return min(dp[-1])

s = Solution()
print(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
                
