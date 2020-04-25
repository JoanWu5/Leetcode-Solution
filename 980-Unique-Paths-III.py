class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.result = 0
        m = len(grid)
        n = len(grid[0])
        empty = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty+=1
                elif grid[i][j] ==1:
                    starti = i
                    startj = j
                elif grid[i][j] ==2:
                    end = (i,j)

        def dfs(x,y,empty):
            if not(0<=x<m and 0<=y<n and grid[x][y]>=0):
                return
            if (x,y) == end:
                self.result+= empty==0
                return
            grid[x][y] = -2
            dfs(x+1,y,empty-1)
            dfs(x-1,y,empty-1)
            dfs(x,y-1,empty-1)
            dfs(x,y+1,empty-1)
            grid[x][y] =0

        dfs(starti,startj,empty)
        return self.result

s = Solution()
print(s.uniquePathsIII( [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
        