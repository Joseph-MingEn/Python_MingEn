class Solution(object):
    def findSpecialInteger(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count_dict = {}
        quarter = len(arr) // 4
        for i in arr:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict.update({i : 1})    

        for key, value in count_dict.items():
            if value > quarter:
                return key
    
n = [1,2,2,6,6,6,6,7,10]
ans = Solution.findSpecialInteger(n)
print(ans)