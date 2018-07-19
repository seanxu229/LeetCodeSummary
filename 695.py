'''
打字的时候注意标点是半角！！！！！！！！
边界情况要考虑到位啊！！！！！
下标不要出界啊！！！！！！
外层函数下标界内，但另外写函数要重新考虑边界啊啊啊啊，因为有可能又已经出界了啊啊啊
'''
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        res=[]
        m=len(grid)
        n=len(grid[0])
        
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j]=0
                return 1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)
            else:
                return 0    
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res.append(dfs(i,j))
        if res:
            return max(res)
        else:
            return 0