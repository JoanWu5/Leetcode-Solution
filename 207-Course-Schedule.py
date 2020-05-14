from collections import defaultdict
class Solution(object):
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.V = numCourses
        self.graph = defaultdict(list)
        for i in range(len(prerequisites)):
            self.addEdge(prerequisites[i][0],prerequisites[i][1])
        
        visited = [0]*numCourses
        for i in range(self.V):
            if self.isCircle(i,visited):
                return False
        return True

    def isCircle(self,start_node,visited):
        if visited[start_node] == -1:
            return True
        if visited[start_node] == 1:
            return False
        visited[start_node] = -1
        for v in self.graph[start_node]:
            if self.isCircle(v,visited):
                return True
        visited[start_node] = 1
        return False

s = Solution()
print(s.canFinish(2,[[1,0]]))