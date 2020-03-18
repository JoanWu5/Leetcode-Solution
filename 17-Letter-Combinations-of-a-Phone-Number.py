class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def backtract(combination,next_digits):
            print(next_digits)
            if len(next_digits)==0:
                result.append(combination)
            else:
                for i in mapping[next_digits[0]]:
                    backtract(combination+i,next_digits[1:])

        mapping = {'2':['a','b','c'], \
                    '3':['d','e','f'],\
                    '4':['g','h','i'],\
                    '5':['j','k','l'],\
                    '6':['m','n','o'],\
                    '7':['p','q','r','s'],\
                    '8':['t','u','v'],\
                    '9':['w','x','y','z']}
        result = []
        
        if digits:
            backtract("",digits)
        return result

s = Solution() 
result = s.letterCombinations("23")
print(result)

        
