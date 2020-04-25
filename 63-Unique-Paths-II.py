class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)]for i in range(m)]
        dp[0][0] =1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] =-1
        for i in range(m):
            for j in range(n):
                if dp[i][j] ==-1 or (i==0 and j==0):
                    continue
                if i==0 and j>0:
                    dp[i][j] = dp[i][j-1]
                elif j ==0 and i>0:
                    dp[i][j] = dp[i-1][j]
                else:
                    if dp[i-1][j] == -1 and dp[i][j-1] == -1:
                        dp[i][j] = -1
                    elif dp[i-1][j] == -1:
                        dp[i][j] =dp[i][j-1]
                    elif dp[i][j-1] ==-1:
                        dp[i][j] =dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]+dp[i][j-1]

        if dp[m-1][n-1] == -1:
            return 0 
        return dp[m-1][n-1]

s = Solution()
print(s.uniquePathsWithObstacles([[0,0]]))
        