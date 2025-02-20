class Solution(object):
    def generateMatrix(n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        ans = [[0 for _ in range(n)] for _ in range(n)]
        dirs = [0, n - 1, 0, n - 1]
        count = n
        num = 0
        total = n * n

        while num <= total:
            for i in range(dirs[0], dirs[1] + 1):
                ans[dirs[2]][i] = num
                num += 1
            dirs[2] += 1

            for i in range(dirs[2], dirs[3] + 1):
                ans[i][dirs[1]] = num
                num += 1
            dirs[1] -= 1
            
            for i in range(dirs[1], dirs[0] - 1,  -1):
                ans[dirs[3]][i] = num
                num += 1
            dirs[3] -= 1

            for i in range(dirs[3], dirs[2] - 1, -1):
                ans[i][dirs[0]] = num
                num += 1
            dirs[0] += 1

        return ans
    
n = 5
ans = Solution.generateMatrix(n)
print(ans)