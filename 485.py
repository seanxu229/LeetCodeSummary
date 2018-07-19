'''
抄的答案。注意多用else啊啊啊啊
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # countlist=[]
        # i=0
        # while i <len(nums):
        #     count=0
        #     while (i <len(nums))&(nums[i]==1):
        #         count=count+1
        #         i=i+1
        #     if count>0:
        #         countlist.append(count)
        #     i=i+1
        # return max(countlist)
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans