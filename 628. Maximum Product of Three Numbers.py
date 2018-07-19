'''
注意这道题目的坑！！！！没有说明都是正数还是负数，有正有负！！！！
'''

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])