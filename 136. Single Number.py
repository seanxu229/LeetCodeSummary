'''
自己的方法巨烂无比。。。。。时间太久
用dictionary的方法更好
'''

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=list(set(nums))+list(set(nums))
        for i in nums:
            if i in a:
                a.remove(i)
        return a[0]

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key