'''build a set() to note all the nodes 
that already traveled before.
check if it's equal to target
!!!set()only have add(), not append()
'''



class Solution:
	def findTarget(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: bool
		"""
		if root==None:
			return False
		s=set()
		stree=[root]
		for i in stree:
			if k-i.val in s:
		return True
		s.add(i.val)
		if i.left:
			stree.append(i.left)
		if i.right:
			stree.append(i.right)
		return False