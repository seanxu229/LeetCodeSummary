'''
认真读题目，读懂题目意思，不要急着想，先完全理解再思考
下标边界想清楚，本题边界不用比较，所以需要len再-1
'''
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(0,len(matrix)-1):
            for j in range(0,len(matrix[0])-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True