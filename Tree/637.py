'''BFS idea
for each level, we have que, compute the mean to the ans
build a new que nque which is a corresponding que to the old que. store the children of the old que
'''
class Solution:
	def averageOfLevels(self, root):
	"""
	:type root: TreeNode
	:rtype: List[float]
	"""
		ans=[]
		que=[root]
		while que:
			ssum=0
			for i in que:
				ssum+=i.val
			ans.append(ssum/len(que))
			nque=[]
			for j in que:
				if j.left:
					nque.append(j.left)
				if j.right:
					nque.append(j.right)
			que=nque
		return ans