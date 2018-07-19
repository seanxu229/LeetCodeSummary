'''
第一种方法自己做的：注意前两个if case不要忘记了！！！
第二种方法时间效率更棒，只遍历一遍，每一步把所有要做的都做了！！
'''

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #mm=max(nums)
        if len(nums)==1:
            return -1
        if len(nums)==1:
            return 0
        mm=max(nums)
        index=nums.index(mm)
        nums.remove(mm)
        if mm>=2*max(nums):
            return index
        return -1


class Solution:
    def dominantIndex(self, nums):
        if len(nums) == 0: return -1

        highest = -1
        secondHighest = -1
        highestIndex = 0
        
        for i,n in enumerate(nums):
            if n >= highest:
                secondHighest = highest
                highest = n
                highestIndex = i
            elif n > secondHighest:
                secondHighest = n

        if highest < secondHighest*2:
            highestIndex = -1
        
        return highestIndex
