'''BFS：check each level.
!!!!!check empty tree!!!
recursion:
it's much better!
调用时不要忘了self
'''

recursion:
class Solution:
	def maxDepth(self, root):
	"""
	:type root: TreeNode
	:rtype: int
	"""
		if root==None:
			return 0
		ld=self.maxDepth(root.left)
		rd=self.maxDepth(root.right)
		return 1+max(ld,rd)

BFS：
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