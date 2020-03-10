import collections
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #version 1
        # d = {}
        # result = []
        # for num in nums:
        #     if num in d:
        #         d[num] +=1
        #     else:
        #         d[num] = 1
        
        # dictk = sorted(d.items(),key=lambda item:item[1],reverse=True)
        # dictk = dictk[:k]
        # for dk in dictk:
        #     result.append(dk[0])
        # return result

        #version 2 :use heap & collections
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get)

s = Solution()
result = s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
print(result)
