class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # num = 0
        # for digit in digits:
        #     num = num*10+digit
        # num = num+1
        # result = []
        # while True:
        #     if num>=1:
        #         result.append(num%10)
        #         num = num//10
        #     else:
        #         break
        # return list(reversed(result))

        for i in range(len(digits)-1,-1,-1):
            num = digits[i]+1
            if num>9:
                digits[i] = 0
                if i == 0:
                    digits = [1]+digits
            else:
                digits[i] +=1
                break
        return digits
        
s = Solution()
print(s.plusOne([1,2,3]))
