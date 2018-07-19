'''
这里注意用set，set是没有.sort函数的。用了sorted(set)以后得到
的实际是一个list
并且要知道set是没有办法slicing的
'''
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=set(nums)
        if len(n)<3:
            return max(nums)
        b=sorted(n)
        return b[-3]