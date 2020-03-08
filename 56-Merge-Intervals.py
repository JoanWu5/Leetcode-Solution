class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <=1:
            return intervals
        
        def get_first(a_list):
            return a_list[0]
        intervals.sort(key=get_first)

        result = [intervals[0]]
        for i in range(1,len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1] = [result[-1][0],max(result[-1][1],intervals[i][1])]
            else:
                result.append(intervals[i])
        return result

s = Solution()
result = s.merge([[1,4],[0,4]])
print(result)
            