‘’‘
多用append函数啊啊啊啊
先遍历把所有数放进list， 然后再按要求分别取出
’‘’
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        matlist=[]
        res=[]
        if r*c!=len(nums)*len(nums[0]):
            return nums
        for i in nums:
            for j in i:
                matlist.append(j)
        # #if r*c!=len(matlist)
        # for i in range(r):
        #     res[i]=matlist[i:i+c]
        # return res
        #这种指标的办法失败了，因为无法这样给listlist赋值
        for i in range(r):
            a=c*i
            res.append(matlist[a:a+c])
        return res