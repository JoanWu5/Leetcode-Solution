import collections
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        indices = collections.defaultdict(list)
        for i,num in enumerate(arr):
            indices[num].append(i)
        done = {-1}
        now = {0}
        step = 0
        while True:
            done |=now
            if len(arr)-1 in done:
                return step
            step +=1
            # temp = now.copy()
            # for i in temp:
            #     if i-1>=0:
            #         now.add(i-1)
            #     if i+1<len(arr):
            #         now.add(i+1)
            #     for item in indices.pop(arr[i],[]):
            #         now.add(item)
            # now -= done
            now = {j for i in now for j in [i-1,i+1]+indices.pop(arr[i],[])}-done

s = Solution()
print(s.minJumps([11,22,7,7,7,7,7,7,7,22,13]))