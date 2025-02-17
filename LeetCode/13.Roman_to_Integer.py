class Solution(object):
    @staticmethod
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        sdic = {}
        ans = 0
        for index, cher in enumerate(s):
            sdic.update({index : cher})
            
        for i in range(len(s)):
            if sdic.get(i) == 0:
                continue
        
            if sdic.get(i) == "I" and (sdic.get(i + 1) == "V" or sdic.get(i + 1) == "X"):
                if sdic.get(i + 1) == "V":
                    ans += 4
                else:
                    ans += 9
                    
                sdic[i] = 0
                sdic[i + 1] = 0
                i += 1
            
            if sdic.get(i) == "X" and (sdic.get(i + 1) == "L" or sdic.get(i + 1) == "C"):
                if sdic.get(i + 1) == "L":
                    ans += 40
                else:
                    ans += 90
                sdic[i] = 0
                sdic[i + 1] = 0
                i += 1
            
            if sdic.get(i) == "C" and (sdic.get(i + 1) == "D" or sdic.get(i + 1) == "M"):
                if sdic.get(i + 1) == "D":
                    ans += 400
                else:
                    ans += 900
                sdic[i] = 0
                sdic[i + 1] = 0
                i += 1

            if sdic.get(i) == "I": 
                ans += 1
            if sdic.get(i) == "V": 
                ans += 5
            if sdic.get(i) == "X": 
                ans += 10
            if sdic.get(i) == "L": 
                ans += 50
            if sdic.get(i) == "C": 
                ans += 100
            if sdic.get(i) == "D": 
                ans += 500
            if sdic.get(i) == "M": 
                ans += 1000
                
        return ans

Input = ["III", "LVIII", "MCMXCIV"]
for i in Input:
    ans = Solution.romanToInt(i)
    print(ans)