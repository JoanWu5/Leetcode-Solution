import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #version 1:
        # m = len(grid)
        # n = len(grid[0])
        # if m == 0:
        #     return []
        # dp = [[0 for j in range(n)] for i in range(m)]
        # for i in range(0,m):
        #     for j in range(0,n):
        #         if i==0 and j==0:
        #             dp[i][j] = grid[0][0]
        #         elif i == 0:
        #             dp[i][j] = dp[i][j-1]+grid[i][j]
        #         elif j == 0 :
        #             dp[i][j] = grid[i][j]+dp[i-1][j]
        #         else:
        #             dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        # return dp[m-1][n-1]

        #version 2
        m = len(grid)
        n = len(grid[0])
        dp = [sys.maxsize for j in range(n)]
        dp[0] = 0
        for i in range(0,m):
            for j in range(0,n):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j],dp[j-1])+grid[i][j]
        return dp[n-1]
        

s = Solution()
result = s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(result)
                
            