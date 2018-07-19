'''
小心summ=0的位置！！开始时就把summ=0放在了最开始，导致超时，结果一直不出来
'''


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num))>1:
            summ=0
            while num >0:
                summ+=num%10
                num=num//10
            num=summ
        return num