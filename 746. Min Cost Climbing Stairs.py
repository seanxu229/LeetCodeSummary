'''
DP 不一定非要写函数，定义一个数组也许就已经够用了
下标的界以及顺序非常重要！！！
'''


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        TC=[0]*(len(cost)+2)
        for i in range(len(cost)-1,-1,-1):
            TC[i]=cost[i]+min(TC[i+1],TC[i+2])
        return min(TC[0],TC[1])