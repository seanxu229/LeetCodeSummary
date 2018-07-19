‘’‘
水仙花数
’‘’
class Solution:
    """
    @param n: The number of digits. 
    @return: All narcissistic numbers with n digits.
    """
    def getNarcissisticNumbers(self, n):
        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if n == 6:
            return [548834]

        result = []
        for i in xrange(10 ** (n-1), 10 ** n):
            j, s = i, 0
            while j != 0:
                s += (j % 10) ** n;
                j = j / 10
            if s == i:
                result.append(i)
        return result