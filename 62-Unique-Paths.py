class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #version 1 : Cm+n-2 n-1
        # if m==1 or n==1:
        #     return 1
        # if m<n:                                                                            
        #     m,n = n,m
        # k = m+n-2
        # up = 1
        # for i in range(m,k+1):
        #     up *= i
        # down = 1
        # for i in range(1,n):
        #     down *=i
        # return int(up/down)

        #version 2:动态规划 dp[i][j]=dp[i-1][j]+dp[i][j-1] 空间复杂度：O(n^2)
        # path = [[1 for col in range(n)] for row in range(m)]
        # for i in range(1,m):
        #     for j in range(1,n):
        #         path[i][j] = path[i-1][j]+path[i][j-1]
        # return path[m-1][n-1]

        #version 3: 动态规划简化版 空间复杂度优化到O(n)
        dp = [1 for col in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j]+dp[j-1]
        return dp[n-1]


s = Solution()
result = s.uniquePaths(7,3)
print(result)