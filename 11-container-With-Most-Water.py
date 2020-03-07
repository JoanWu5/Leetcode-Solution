class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #version1 : 0(n2)
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(range(len(height)))):
        #         max_area =max(max_area, min(height[i],height[j])*(j-i))
        # return max_area

        #version 2 
        head_p = 0
        tail_p = len(height)-1
        max_area = 0
        while head_p < tail_p:
            max_area =max(max_area, min(height[head_p],height[tail_p])*(tail_p-head_p))
            if height[head_p] < height[tail_p]:
                head_p += 1
            else:
                tail_p -= 1
        return max_area
        
s= Solution()
result = s.maxArea([1,8,6,2,5,4,8,3,7])
print(result)