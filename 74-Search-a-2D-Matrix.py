class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) ==0 or matrix[0] is None  or len(matrix[0])==0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = m-1
        j = 0
        while i<m and i>=0 and j<n and j>=0:
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j]<target:
                    j+=1
                else:
                    i-=1
        return False

s = Solution()
print(s.searchMatrix([[1,3,5]],0))