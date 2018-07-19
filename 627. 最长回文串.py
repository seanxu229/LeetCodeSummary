'''
对原list做一次大遍历。
成双成对出现的的滚出去，拉下的单留在temp数组里。
滚出去的一定在回文数里。拉单的中拿出一个当回文数中心即可
'''
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        temp=[]
        count=0
        b=0
        for i in s:
            if i not in temp:
                temp.append(i)
            else:
                count+=1
                temp.remove(i)
        if len(temp)!=0:
            b=1
        return (len(s)-len(temp))+b