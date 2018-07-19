'''
第一个if是为了防止最末尾的数没有在里面。因为最后的那个大数
无法放进for loop， 放进去会out of index range
'''
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) not in nums:
            return len(nums)
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i