'''
用while循环记录
'''

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i=0
        res=[]
        while i<len(S):
            j=i+1
            while j<len(S) and S[i]==S[j]:
                j+=1
            if j-i>2:
                res.append([i,j-1])
            i=j
        return res