class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        s0 = str(x)
        s1 = s0[::-1]
        isPalindrome = False

        if s0 == s1:
            isPalindrome = True
        
        return isPalindrome
    
Input = [121, -121, 10]
for i in Input:
    ans = Solution.isPalindrome(i)

    print(ans)