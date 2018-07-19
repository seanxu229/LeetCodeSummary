'''
自己本来的方法效率太低，超过时间限制了
这种HASHSET的方法就是建立一个移动的HashSet
'''



class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<=k:
            return len(nums) >  len(set(nums))
        hashset=set(nums[:k])
        if len(hashset)<k:
            return True
        
        for i in range(k,len(nums)):
            hashset.add(nums[i])
            if len(hashset)==k:
                return True
            else:
                hashset.remove(nums[i-k])
        return False