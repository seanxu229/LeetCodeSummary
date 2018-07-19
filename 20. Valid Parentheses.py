'''
括号是否valid实现
2种方法
利用stack：
建立一个字典，前后括号对应起来。
遇到一半的括号现存入stack，遇到后半段括号，检查：
很重要！！！
！！！stack里是否有前半段括号，没有就false这个考虑不全面
检查stack里的最后pop是不是和后半段括号对应！！若不，return False
有其他东西乱入 return False

最终stack全部有对应，i.e. stack为空，则返回True 

'''
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

‘’‘
比较讨巧的方法，但不易想到
’‘’
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False