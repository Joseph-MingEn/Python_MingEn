class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            r = target - nums[i]
            for j in range(len(nums) - i):
                if i + j + 1 < len(nums):
                    a = nums[i + j + 1]
                    if r == a:
                        return [i, i+j+1]
                    
InputNums  = {
        0 : [2,7,11,15]
        , 1 : [3,2,4]
        , 2 : [3,3]
        }
InputTarget = {
        0 : 9
        , 1 : 6
        , 2 : 6
        }

for i in range(3):
    ans = Solution.twoSum(InputNums[i], InputTarget[i])
    print(ans)