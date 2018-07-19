'''
第一种方法递归时间超时了
第二种方法别忘了前面两个if，不然当test n=1是结果是错误的
'''
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        # if n==2:
        #     return 1
        # if n==1:
        #     return 0
        # else:
        #     return self.fibonacci(n-1)+self.fibonacci(n-2)
        res=[]
        res.append(0)
        res.append(1)
        if n==1:
            return 0 
        if n==2:
            return 1
        for i in range(n-2):
            x=res[-1]
            y=res[-2]
            res.append(x+y)
        return res[-1]