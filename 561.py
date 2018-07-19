'''
熟悉python内部自建函数n.sort()与sorted(n)
读清楚题目意思及步骤
'''
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res=0
        for i in range(0,len(nums),2):
            res+=nums[i]
        return res
        # return sum(sorted(nums)[::2])