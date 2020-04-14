class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""
        if numerator/denominator<0:
            result +="-"
        if numerator%denominator ==0:
            return str(numerator//denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        result +=str(numerator//denominator)+"."
        numerator %=denominator
        i = len(result)
        table = {}
        while numerator!=0:
            if numerator not in table.keys():
                table[numerator] = i
            else:
                i = table[numerator]
                result = result[:i]+"("+result[i:]+")"
                return result
            numerator = numerator*10
            result +=str(numerator//denominator)
            numerator %=denominator
            i+=1
        return result

s = Solution()
print(s.fractionToDecimal(1,6))
