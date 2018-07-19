'''
抄的答案，思路非常巧妙，需要记住
掌握zip函数！！
'''
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=str.split()
        if len(s)!=len(pattern):
            return False
        if len(set(zip(pattern,s)))==len(set(pattern))==len(set(s)):
            return True
        else:
            return False