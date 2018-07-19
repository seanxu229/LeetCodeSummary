'''
从第一个数开始起，一个一个遍历判定两端是否相等
'''

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=sum(nums)
        for i in range(len(nums)):
            right-=nums[i]
            if right==left:
                return i
            left+=nums[i]
        return -1