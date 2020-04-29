class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited = [0]*len(arr)
        visited[start] = 1
        def canReach2(arr,start):
            if start+arr[start]<len(arr) and visited[start+arr[start]]==0:
                visited[start+arr[start]]=1
                canReach2(arr,start+arr[start])
            if start-arr[start]>=0 and visited[start-arr[start]]==0:
                visited[start-arr[start]]=1
                canReach2(arr,start-arr[start])
        canReach2(arr,start)
        for i in range(len(arr)):
            if arr[i] == 0 and visited[i] ==1:
                return True
        return False

s = Solution()
print(s.canReach([0,3,0,6,3,3,4],6))
        