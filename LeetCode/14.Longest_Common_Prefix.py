class Solution(object):
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        strMemo = {}

        for i in range(len(strs)):
            strMemo.update({i : strs[i]})
        for index, cher in enumerate(strs[0]):
            count = 0
            for i in range(len(strs)):
                # return cher, strs[index][i]
                try:
                    if cher == strs[i][index]:
                        count += 1
                except IndexError:
                    break
            # return count, len(strs)
            if count == len(strs):
                ans += cher
            else:
                break

        return ans
    

Input = ["flower","flow","flight"]
ans = Solution.longestCommonPrefix(Input)

print(ans)