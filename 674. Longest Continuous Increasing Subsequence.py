'''
不停用max()临时返回存储
'''


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        res=1
        count=1
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                res=max(res,count)
                count=1
            else:
                count+=1
                res=max(res,count)    
        return res
                