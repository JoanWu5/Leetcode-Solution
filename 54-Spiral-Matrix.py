class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def spiral_coords(r1,r2,c1,c2):
            for c in range(c1,c2+1):
                yield r1,c
            for r in range(r1+1,r2+1):
                yield r,c2
            if r1<r2 and c1<c2:
                for c in range(c2-1,c1,-1):
                    yield r2,c
                for r in range(r2,r1,-1):
                    yield r,c1

        if matrix is None or matrix == []:
            return []
        c1 = 0
        c2 = len(matrix[0])-1
        r1 = 0
        r2 =len(matrix)-1
        result = []
        while r1<=r2 and c1<=c2:
            for r,c in spiral_coords(r1,r2,c1,c2):
                result.append(matrix[r][c])
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return result

s = Solution()
print(s.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]))

