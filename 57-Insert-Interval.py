class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        #version 1:O(nlogn)
        # if newInterval == []:
        #     return intervals
        # intervals.append(newInterval)
        # result = []
        # for i in sorted(intervals,key= lambda x:x[0]):
        #     if result and result[-1][1] >= i[0]:
        #         result[-1][1] = max(result[-1][1],i[1])
        #     else:
        #         result.append(i)
        # return result

        #version 2:O(n)
        result = []
        for index,i in enumerate(intervals):
            if i[1]<newInterval[0]:
                result.append(i)
            elif newInterval[1]<i[0]:
                result.append(newInterval)
                return result+intervals[index:]
            else:
                newInterval[0] = min(i[0],newInterval[0])
                newInterval[1] = max(i[1],newInterval[1])
        result.append(newInterval)
        return result


s = Solution()
print(s.insert([[1,3],[6,9]],[2,5]))
        
        
        
                