'''
自己做出来的！！！并且还挺快就做出来了！！！
eg：有10块糖果，每个人就有5块糖果。
然后这5块糖果的种类个数可以是1-5，让sister尽可能有多的种类，
那么就让set(candies)尽量都分给sister。如果种类多就5个，
种类少就种类有多少就都给妹妹
'''

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)),len(candies)//2)