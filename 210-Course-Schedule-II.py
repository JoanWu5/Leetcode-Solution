from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        d = [0]*numCourses
        graph = defaultdict(list)   
        for i, j in prerequisites:
            d[i] +=1
            graph[j].append(i)
        stack = [i for i in range(numCourses) if d[i] == 0]
        result = []
        while stack:
            node = stack.pop()
            result.append(node)
            for i in graph[node]:
                d[i]-=1
                if d[i]==0:
                    stack.append(i)
        if sum(d)>0:
            return []
        return result

s = Solution()
print(s.findOrder(2,[[1,0]]))