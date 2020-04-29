class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost)>sum(gas):
            return -1
        sum1 = 0
        k = 0
        total = 0
        for i in range(len(gas)):
            sum1 +=gas[i]-cost[i]
            if sum1<0:
                total +=sum1
                k = i+1
                sum1 = 0
        total+=sum1
        if total<0:
            return -1
        return k

s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))