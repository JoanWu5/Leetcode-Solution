class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        d = {}
        result = []
        for h,k in people:
            if h in d:
                d[h].append([h,k])
            else:
                d[h] = ([[h,k]])
        print(d)
        for h in sorted(d.keys(),reverse= True):
            group = sorted(d[h])
            print(group)
            for h,k in group:
                result.insert(k,[h,k])
        return result
s= Solution()
print(s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
        