'''
仔细检查下标
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res=0
        i=0
        while i <len(prices)-1:
            #这里的price（i+1）是容易out of index range的所以
            #上面while那个length要减1
            if prices[i]<prices[i+1]:
                res+=prices[i+1]-prices[i]
            i+=1
        return res