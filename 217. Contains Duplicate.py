'''
很简单的题目，强制set()以后比较list和set的长度即可
'''


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(nums)==len(set(nums))