class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0 :
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = m-1
        j = 0
        while target < matrix[i][j] and i>=0:
            i -=1
        while j< n:
            if target == matrix[i][j]:
                return True
            if target >matrix[i][j]:
                j +=1
            else:
                if i>0:
                    i -=1
                else:
                    return False
        return False

s = Solution()
result = s.searchMatrix([[-5]],-10)
print(result)


