class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        #version 1: Time Limited Exceeded
        # result = [0 for i in range(len(T))]
        # for i in range(len(T)):
        #     for j in range(i+1,len(T)):
        #         if T[j] > T[i]:
        #             result[i] = j-i
        #             break
        # return result

        #version 2: stack
        n = len(T)
        result,stack = [0]*n,[]
        for i in range(n-1,-1,-1):
            if stack==[]:
                stack.append(i)
            else:
                while stack and T[i] >= T[stack[-1]]:
                    stack.pop()
                if stack !=[]:
                    result[i] = stack[-1] - i
                stack.append(i)
        return result 


s = Solution()
result = s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70])
print(result)